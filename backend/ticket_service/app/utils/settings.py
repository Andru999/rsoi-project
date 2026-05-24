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
    """Получение строки подключения к БД."""
    settings = get_settings(config_name)

    return (
        f"postgresql://{settings['databases']['ticket_db']['user']}:"
        f"{settings['databases']['ticket_db']['password']}@"
        f"{settings['databases']['ticket_db']['host']}:"
        f"{settings['databases']['ticket_db']['port']}/"
        f"{settings['databases']['ticket_db']['db']}"
    )
