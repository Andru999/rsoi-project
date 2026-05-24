import bcrypt
from exceptions.http import BadRequestException, NotAuthorizedException
from jwcrypto.jws import InvalidJWSSignature
from jwcrypto.jwt import JWTExpired
from model.user import UserModel
from utils.enums import (
    BadRequestErrorTextEnum,
    LoginErrorTextEnum,
    PayloadEnum,
    TokenTypeEnum,
)
from utils.jwt import auth_jwt


def validate_user_login_in_users(
    login: str,
    users: list[UserModel],
) -> UserModel:
    for user in users:
        if user.login == login:
            return user

    raise NotAuthorizedException(
        error_in=LoginErrorTextEnum.INVALID_LOGIN,
    )


def validate_password(
    password: str,
    hashed_password: bytes,
) -> None:
    if not bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    ):
        raise NotAuthorizedException(
            error_in=LoginErrorTextEnum.INVALID_PASSWORD,
        )


def validate_token_decode(
    token: str | None,
) -> dict:
    if token is None:
        raise NotAuthorizedException(error_in=LoginErrorTextEnum.NO_TOKEN)
    try:
        user_raw = auth_jwt.decode_jwt(token)
    except ValueError as err:
        raise NotAuthorizedException(
            error_in=LoginErrorTextEnum.INVALID_TOKEN_FORMAT,
        ) from err
    except InvalidJWSSignature as err:
        raise NotAuthorizedException(
            error_in=LoginErrorTextEnum.INVALID_PUBLIC_KEY,
        ) from err
    except JWTExpired as err:
        raise NotAuthorizedException(
            error_in=LoginErrorTextEnum.TOKEN_HAS_EXPIRED,
        ) from err

    return user_raw


def validate_token_type(
    payload: dict,
    token_type: TokenTypeEnum,
) -> None:
    try:
        if payload[PayloadEnum.TOKEN_TYPE] != token_type:
            raise BadRequestException(
                error_in=BadRequestErrorTextEnum.INVALID_TOKEN_TYPE,
                detail=TokenTypeEnum.REFRESH
                if token_type == TokenTypeEnum.ACCESS
                else TokenTypeEnum.ACCESS,
            )
    except KeyError as err:
        raise BadRequestException(
            error_in=BadRequestErrorTextEnum.INVALID_PAYLOAD_FIELD,
            detail=err,
        ) from err
