import json
from datetime import datetime, timedelta, timezone

from jwcrypto.jwt import JWT
from model.user import UserModel
from utils.enums import HeaderEnum, JWTScopeEnum, PayloadEnum, TokenTypeEnum
from utils.jwks import auth_jwk
from utils.settings import settings


class AuthJWT:
    @staticmethod
    def get_access_token(
        user: UserModel,
        scope: list[str] | None = None,
    ) -> str:
        jwt_header = AuthJWT.__create_header()
        jwt_payload = AuthJWT.__create_payload(
            user,
            TokenTypeEnum.ACCESS,
            scope,
        )

        return AuthJWT.encode_jwt(
            header=jwt_header,
            payload=jwt_payload,
        )

    @staticmethod
    def get_refresh_token(
        user: UserModel,
    ) -> str:
        jwt_header = AuthJWT.__create_header()
        jwt_payload = AuthJWT.__create_payload(
            user,
            TokenTypeEnum.REFRESH,
            expire_minutes=settings.options.auth_jwt.refresh_token_expire_minutes,
        )

        return AuthJWT.encode_jwt(
            header=jwt_header,
            payload=jwt_payload,
        )

    @staticmethod
    def __create_service_payload(
        token_type: TokenTypeEnum,
        expire_minutes: int = settings.options.auth_jwt.access_token_expire_minutes,  # noqa: E501
        expire_timedelta: timedelta | None = None,
    ) -> dict:
        now = datetime.now(timezone.utc)
        if expire_timedelta:
            expire = now + expire_timedelta
        else:
            expire = now + timedelta(minutes=expire_minutes)

        return {
            PayloadEnum.TOKEN_TYPE: token_type,
            PayloadEnum.IAT: int(now.timestamp()),
            PayloadEnum.EXP: int(expire.timestamp()),
        }

    @staticmethod
    def __create_payload(
        user: UserModel,
        token_type: TokenTypeEnum,
        scope: list[str] | None = None,
        expire_minutes: int = settings.options.auth_jwt.access_token_expire_minutes,  # noqa: E501
        expire_timedelta: timedelta | None = None,
    ) -> dict:
        jwt_payload = AuthJWT.__create_service_payload(
            token_type=token_type,
            expire_minutes=expire_minutes,
            expire_timedelta=expire_timedelta,
        )

        jwt_payload.update(
            {
                PayloadEnum.SUB: str(user.uuid),
            },
        )

        if token_type == TokenTypeEnum.REFRESH:
            return jwt_payload

        if token_type == TokenTypeEnum.ACCESS:
            jwt_payload.update(
                {
                    PayloadEnum.LOGIN: user.login,
                    PayloadEnum.ROLE: user.role,
                },
            )

            if scope is None:
                return jwt_payload

            for data in scope:
                if data == JWTScopeEnum.OPENID:
                    continue  # базовый payload access

                if data == JWTScopeEnum.EMAIL:
                    jwt_payload.update(
                        {
                            PayloadEnum.EMAIL: user.email,
                        },
                    )
                elif data == JWTScopeEnum.PROFILE:
                    jwt_payload.update(
                        {
                            PayloadEnum.LASTNAME: user.lastname,
                            PayloadEnum.FIRSTNAME: user.firstname,
                            PayloadEnum.PHONE: user.phone,
                        },
                    )

        return jwt_payload

    @staticmethod
    def __create_header(
        algorithm: str = settings.options.auth_jwt.algorithm,
        typ: str = settings.options.auth_jwt.typ,
        kid: str = settings.options.jwks.kid,
    ) -> dict:
        return {
            HeaderEnum.ALG: algorithm,
            HeaderEnum.TYP: typ,
            HeaderEnum.KID: kid,
        }

    @staticmethod
    def encode_jwt(  # noqa: ANN205
        header: dict,
        payload: dict,
        jwk_kid: str = settings.options.jwks.kid,
    ):
        token = JWT(
            header=header,
            claims=payload,
        )

        jwks_dict = auth_jwk.get_jwks_from_file(private_keys=True)
        jwks = auth_jwk.transform_dict_to_jwks(jwks_dict)
        key = auth_jwk.get_by_kid(jwks, jwk_kid)

        token.make_signed_token(
            key=key,
        )

        return token.serialize()

    @staticmethod
    def decode_jwt(
        token: str | bytes,
    ) -> JWT:
        jwks_dict = auth_jwk.get_jwks_from_file()
        jwks = auth_jwk.transform_dict_to_jwks(jwks_dict)

        jwt = JWT()
        jwt.deserialize(jwt=token, key=jwks)

        return json.loads(jwt.claims)


auth_jwt = AuthJWT()
