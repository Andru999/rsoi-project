import json
from pathlib import Path

from jwcrypto.jwk import JWK, InvalidJWKValue, JWKSet
from utils.settings import settings


class AuthJWK:
    @staticmethod
    def get_jwks_from_file(
        private_keys: bool = False,
        jwks_file_path: Path = settings.options.jwks.jwks_path,
    ) -> dict | str | None:
        try:
            with Path.open(jwks_file_path, "r") as jwks_file:
                jwks = JWKSet.from_json(jwks_file.read())

            return jwks.export(private_keys=private_keys, as_dict=True)
        except FileNotFoundError:
            return None
        except InvalidJWKValue:
            return None

    @staticmethod
    def transform_dict_to_jwks(jwks_dict: dict) -> JWKSet:
        return JWKSet.from_json(keyset=json.dumps(jwks_dict, sort_keys=True))

    @staticmethod
    def generate_jwks(
        number_of_keys: int = settings.options.jwks.keys_to_generate,
        force: bool = False,
    ) -> None:
        jwks = AuthJWK.get_jwks_from_file()

        if jwks and force is False:
            return

        keys: list[JWK] = []
        for kid in range(1, number_of_keys + 1):
            key = JWK.generate(
                kty=settings.options.jwks.kty,
                size=settings.options.jwks.size,
                alg=settings.options.jwks.alg,
                use=settings.options.jwks.use,
                kid=str(kid),
            )
            keys.append(key)

        AuthJWK.export_to_file(keys)

    @staticmethod
    def export_to_file(jwks: list[JWK]) -> None:
        jwks_path = Path(settings.options.jwks.jwks_path)
        jwks_path.parent.mkdir(parents=True, exist_ok=True)  # <--- добавить
        with Path.open(jwks_path, "w") as jwks_file:
            keys = []
            for jwk in jwks:
                keys.append(jwk.export(private_key=True, as_dict=True))
            if keys:
                json.dump({"keys": keys}, jwks_file, indent=2)

    @staticmethod
    def get_by_kid(jwks: JWKSet, kid: str) -> JWK:
        return jwks.get_key(kid=kid)


auth_jwk = AuthJWK()
