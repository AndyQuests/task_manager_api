import pytest
import asyncio

@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    async def instant_sleep(seconds: float):
        return None
    
    monkeypatch.setattr(asyncio, "sleep", instant_sleep)