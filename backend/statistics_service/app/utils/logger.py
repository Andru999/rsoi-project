import logging
from datetime import datetime as dt
from datetime import timedelta, timezone
from logging.handlers import SysLogHandler

from fastapi import status
from typing_extensions import Self
from utils.settings import get_settings

logging.Formatter.converter = lambda *args: dt.now(  # noqa: ARG005
    tz=timezone(timedelta(hours=3)),
).timetuple()


class Log:
    def __init__(self: Self, config_name: str = "./config.yaml") -> None:
        self.settings = get_settings(config_name)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        self.formatter = logging.Formatter(
            fmt=self.settings["logger"]["fmt"],
            datefmt=self.settings["logger"]["datefmt"],
        )

        self.sys_handler = self.__create_sys_log_handler()
        self.logger.addHandler(self.sys_handler)

        self.date = dt.now(tz=timezone(timedelta(hours=3))).strftime(
            self.settings["logger"]["file_name"],
        )

        self.file_handler = self.__create_file_handler()
        self.logger.addHandler(self.file_handler)

    def reset_file_handler(self: Self) -> None:
        current_date = dt.now(tz=timezone(timedelta(hours=3))).strftime(
            self.settings["logger"]["file_name"],
        )
        if current_date != self.date:
            self.date = current_date

            self.logger.removeHandler(self.file_handler)
            self.file_handler = self.__create_file_handler()
            self.logger.addHandler(self.file_handler)

    def __create_file_handler(self: Self) -> logging.FileHandler:
        handler = logging.FileHandler(
            filename=f"logs/{self.date}.log",
            mode="a",
        )
        handler.setFormatter(self.formatter)

        return handler

    def __create_sys_log_handler(self: Self) -> SysLogHandler:
        handler = SysLogHandler(
            facility=SysLogHandler.LOG_DAEMON,
            address="/dev/log",
        )
        handler.setFormatter(self.formatter)

        return handler


# app_logger = Log() # noqa: ERA001

status_code_desc_dict = {
    status.HTTP_200_OK: "OK",
    status.HTTP_201_CREATED: "Created",
    status.HTTP_204_NO_CONTENT: "No Content",
    status.HTTP_404_NOT_FOUND: "Not Found",
    status.HTTP_409_CONFLICT: "Conflict",
    422: "Validation Error",
}
