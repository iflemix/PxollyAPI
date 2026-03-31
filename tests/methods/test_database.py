import pytest

from pxolly_api import PxollyAPI
from pxolly_api.enums import DatabaseID
from pxolly_api.models.database import DatabaseGet


@pytest.mark.asyncio
async def test_database_get(pxolly_api: PxollyAPI) -> None:
    result = await pxolly_api.database.get(DatabaseID.IRIS, "733772362", allow_fakes=True)
    assert isinstance(result, DatabaseGet)
