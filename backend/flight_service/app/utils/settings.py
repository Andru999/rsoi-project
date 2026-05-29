from pathlib import Path

from yaml import safe_load

CONFIG_PATH = "config.yaml"


def get_settings(config_name: str = CONFIG_PATH) -> dict:
    """Получение словаря с настройками из конфигурационного файла."""
    if Path(config_name).is_file():
        with Path(config_name).open("r") as f:
            data = safe_load(f)

    return data


def get_db_url(config_name: str = CONFIG_PATH) -> str:
    settings = get_settings(config_name)

    return (
        f"postgresql://{settings['databases']['flightdb']['user']}:"
        f"{settings['databases']['flightdb']['password']}@"
        f"{settings['databases']['flightdb']['host']}:"
        f"{settings['databases']['flightdb']['port']}/"
        f"{settings['databases']['flightdb']['db']}"
    )
