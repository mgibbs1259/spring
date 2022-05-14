import os
import json
import getpass
from pathlib import Path

from ring_doorbell import Auth
from oauthlib.oauth2 import MissingTokenError


def save_updated_token(token: dict) -> None:
    """Saves Ring token."""
    cache_file = Path(os.environ["RING_CACHE_FILE"])
    cache_file.write_text(json.dumps(token))


def conduct_otp_callback() -> str:
    """Obtains Ring 2FA code."""
    return getpass.getpass("Ring 2FA code: ")


def perform_ring_auth() -> Auth:
    """Returns Ring Auth object."""
    cache_file = Path(os.environ["RING_CACHE_FILE"])
    if cache_file.is_file():
        auth = Auth(
            "spring/1.0", json.loads(cache_file.read_text()), save_updated_token
        )
    else:
        username = os.environ["RING_USERNAME"]
        password = os.environ["RING_PASSWORD"]
        auth = Auth("spring/1.0", None, save_updated_token)
        try:
            auth.fetch_token(username, password)
        except MissingTokenError:
            auth.fetch_token(username, password, conduct_otp_callback())
    return auth
