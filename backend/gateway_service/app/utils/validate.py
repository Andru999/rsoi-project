from enums.auth import (
    BadRequestErrorTextEnum,
    LoginErrorTextEnum,
    PayloadEnum,
    TokenTypeEnum,
)
from exceptions.http_exceptions import (
    BadRequestException,
    NotAuthorizedException,
)
from fastapi.security import HTTPAuthorizationCredentials
from jwcrypto.jws import InvalidJWSSignature
from jwcrypto.jwt import JWTExpired
from utils.jwt import decode_jwt


def validate_token_exists(
    token: HTTPAuthorizationCredentials | None,
) -> None:
    if token is None:
        raise NotAuthorizedException(
            error_in=LoginErrorTextEnum.NO_TOKEN,
        )


def validate_token_decode(
    token: str | None,
) -> dict:
    if token is None:
        raise NotAuthorizedException(
            error_in=LoginErrorTextEnum.NO_TOKEN,
        )
    try:
        user_raw = decode_jwt(token)
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
