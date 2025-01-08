import pytest
import httpx

@pytest.mark.asyncio
async def test_root():
    async with httpx.AsyncClient(base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_database_connection():
    from config.database import engine
    async with engine.connect() as conn:
        assert await conn.scalar("SELECT 1") == 1
