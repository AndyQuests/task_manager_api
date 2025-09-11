import pytest
import asyncio

@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    async def instant_sleep(seconds: float):
        return None # instantly return, no waiting
    
    # replace asyncio.sleep with our fake sleep
    monkeypatch.setattr(asyncio, "sleep", instant_sleep)