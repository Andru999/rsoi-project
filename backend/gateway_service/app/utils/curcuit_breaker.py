import requests
import time
from threading import Thread, Lock
from fastapi import status
from collections import deque

from utils.settings import get_settings


class CircuitBreaker:
    settings = get_settings()["services"]["gateway"]

    WINDOW_SIZE = settings.get("sliding_window_size", 4)
    FAIL_THRESHOLD = settings.get("fail_threshold_percent", 50) / 100

    _services = {}
    _waiter: Thread = None
    _lock = Lock()

    @staticmethod
    def send_request(
            url: str,
            http_method,
            headers={},
            data={},
            params=None,
            timeout=5
        ):
        resp = requests.Response()
        resp.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        if http_method is None:
            return resp

        host_url = url[url.find('://') + 3:]
        host_url = host_url[:host_url.find('/')]

        service = CircuitBreaker._services.get(host_url)
        if service is None:
            service = {
                "window": deque(maxlen=CircuitBreaker.WINDOW_SIZE),
                "state": "available",
            }
            CircuitBreaker._services[host_url] = service

        # если сервис в состоянии open (unavailable)
        if service["state"] == "unavailable":
            print(f"[CB] Service {host_url} is unavailable")
            return resp

        try:
            response = http_method(
                url=url,
                headers=headers,
                json=data,
                params=params,
                timeout=timeout
            )
        except Exception:
            CircuitBreaker._register_result(host_url, False)
            return resp

        # успешный (статус < 500)
        if response.status_code < 500:
            CircuitBreaker._register_result(host_url, True)
            return response

        # ошибка >= 500
        CircuitBreaker._register_result(host_url, False)
        return response

    @staticmethod
    def _register_result(host_url: str, is_success: bool):
        with CircuitBreaker._lock:
            service = CircuitBreaker._services[host_url]
            service["window"].append(is_success)

            # если окно ещё не набралось — не переключаемся
            if len(service["window"]) < CircuitBreaker.WINDOW_SIZE:
                return

            # вычисляем долю ошибок
            errors = service["window"].count(False)
            total = len(service["window"])
            err_rate = errors / total

            # если слишком много ошибок — открываем CB
            if err_rate > CircuitBreaker.FAIL_THRESHOLD:
                print(f"[CB] {host_url} FAIL RATE {err_rate*100:.1f}% → OPEN")
                service["state"] = "unavailable"

                if CircuitBreaker._waiter is None:
                    CircuitBreaker._waiter = Thread(
                        target=CircuitBreaker._wait_for_available
                    )
                    CircuitBreaker._waiter.start()

    @staticmethod
    def _wait_for_available():
        timeout = CircuitBreaker.settings["timeout"]
        while True:
            time.sleep(timeout)
            all_ok = True

            with CircuitBreaker._lock:
                for host_url, service in CircuitBreaker._services.items():
                    if service["state"] == "unavailable":
                        Thread(
                            target=CircuitBreaker._check_health,
                            args=(host_url,)
                        ).start()
                        all_ok = False

            if all_ok:
                break

        CircuitBreaker._waiter = None

    @staticmethod
    def _check_health(host_url: str):
        url = f"http://{host_url}/api/v1/manage/health"
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == status.HTTP_200_OK:
                with CircuitBreaker._lock:
                    print(f"[CB] {host_url} → CLOSED")
                    CircuitBreaker._services[host_url]["state"] = "available"
                    CircuitBreaker._services[host_url]["window"].clear()
        except Exception:
            print("[CB] Error health:", url)

