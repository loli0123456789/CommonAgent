import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import httpx
from src.main import app

@pytest.fixture
async def client():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
