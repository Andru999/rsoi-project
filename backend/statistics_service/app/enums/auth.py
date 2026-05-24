from strenum import StrEnum


class RoleEnum(StrEnum):
    USER = "USER"
    MODERATOR = "MODERATOR"
    ADMIN = "ADMIN"


class LoginErrorTextEnum(StrEnum):
    INVALID_LOGIN = "Неверный логин"
    INVALID_PASSWORD = "Неверный пароль"
    INVALID_TOKEN_FORMAT = "Неверный формат токена"
    INVALID_PUBLIC_KEY = "Неверный публичный ключ для расшифровки"
    TOKEN_HAS_EXPIRED = "Время жизни токена закончилось"
    NO_TOKEN = "Токен не передан"


class BadRequestErrorTextEnum(StrEnum):
    INVALID_PAYLOAD_FIELD = "Неверные поля payload"
    INVALID_TOKEN_TYPE = "Неверный тип токена"


class TokenTypeEnum(StrEnum):
    ACCESS = "access"
    REFRESH = "refresh"


class PayloadEnum(StrEnum):
    SUB = "sub"
    LOGIN = "login"
    ROLE = "role"
    EMAIL = "email"
    LASTNAME = "lastname"
    FIRSTNAME = "firstname"
    PHONE = "phone"
    # Service Fields
    TOKEN_TYPE = "type"
    EXP = "exp"  # время, когда токен истечет
    IAT = "iat"  # время, когда токен был выпущен
