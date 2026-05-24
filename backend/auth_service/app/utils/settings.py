from pathlib import Path

from pydantic import BaseModel
from yaml import safe_load

BASE_DIR = Path(__file__).parent.parent
CERTS_DIR_NAME = "certs"
CONFIG_PATH = "config.yaml"


class ServiceSettings(BaseModel):
    host: str = None
    port: int = None
    log_level: str = None
    reload: bool = None


class DatabaseSettings(BaseModel):
    user: str = None
    password: str = None
    host: str = None
    port: int = None
    db_name: str = None


class AuthJWTSettings(BaseModel):
    typ: str = "JWT"
    algorithm: str = "RS256"  # так как ключи Private и Public / иначе HS256
    access_token_expire_minutes: int = 15
    refresh_token_expire_minutes: int = 60


class JWKSSettings(BaseModel):
    jwks_path: Path = BASE_DIR / CERTS_DIR_NAME / "jwks.json"
    keys_to_generate: int = 1
    kty: str = "RSA"
    size: int = 2048
    alg: str = "RSA256"
    use: str = "sig"
    kid: str = (
        None  # из глобальных настроек, чтобы также менять во всех сервисах
    )


class SettingOptions(BaseModel):
    service: ServiceSettings = ServiceSettings()
    database: DatabaseSettings = DatabaseSettings()
    auth_jwt: AuthJWTSettings = AuthJWTSettings()
    jwks: JWKSSettings = JWKSSettings()


class Settings:
    options: SettingOptions = SettingOptions()

    def __init__(self, config_name: str = CONFIG_PATH) -> None:
        if Path(config_name).is_file():
            with Path(config_name).open("r") as f:
                data = safe_load(f)
            try:
                service = data["services"]["auth"]
                Settings.options.service.host = service["host"]
                Settings.options.service.port = service["port"]
                Settings.options.service.log_level = service["log_level"]
                Settings.options.service.reload = service["reload"]

                database = data["databases"]["auth_db"]
                Settings.options.database.user = database["user"]
                Settings.options.database.password = database["password"]
                Settings.options.database.host = database["host"]
                Settings.options.database.port = database["port"]
                Settings.options.database.db_name = database["db"]

                auth_service_data = data["services"]["auth"]
                Settings.options.jwks.kid = auth_service_data["kid"]
            except KeyError as e:
                print(f"SETTINGS: no argument {e}")
            else:
                Settings.__log()

    def __log() -> None:
        print(f"\n{Settings.options.model_dump_json(indent=2)}\n")


settings = Settings()
