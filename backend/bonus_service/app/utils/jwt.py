import json

from jwcrypto.jwk import JWKSet
from jwcrypto.jwt import JWT
from utils.api_requests import get_request
from utils.settings import get_settings


def decode_jwt(
    token: str | bytes,
) -> dict:
    jwks = __get_jwks()
    jwt = JWT()
    jwt.deserialize(jwt=token, key=jwks)

    return json.loads(jwt.claims)


def __transform_dict_to_jwks(jwks_dict: dict) -> JWKSet:
    return JWKSet.from_json(keyset=json.dumps(jwks_dict, sort_keys=True))


def __construct_jwks_auth_url() -> str:
    settings = get_settings()
    host = settings["services"]["auth"]["network_host"]
    port = settings["services"]["auth"]["port"]

    return f"http://{host}:{port}/api/v1/user/.well-known/jwks.json"


def __get_jwks() -> JWKSet:
    url = __construct_jwks_auth_url()
    response = get_request(url=url)

    return __transform_dict_to_jwks(response.json())
