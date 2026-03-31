import os
import typing

import dotenv
import pytest_asyncio

from pxolly_api import PxollyAPI

dotenv.load_dotenv()


@pytest_asyncio.fixture()
async def pxolly_api() -> typing.AsyncGenerator[PxollyAPI]:
    token = os.getenv("PXOLLY_API_TOKEN")
    if not token:
        raise ValueError("Not PXOLLY_API_TOKEN in .env file")

    async with PxollyAPI(token=token) as api:
        yield api
