import os

import dotenv
import pytest

from pxolly_api import PxollyAPI

dotenv.load_dotenv()


@pytest.fixture()
def pxolly_api() -> PxollyAPI:
    token = os.getenv("PXOLLY_TOKEN")
    api = PxollyAPI(token=token)
    return api
