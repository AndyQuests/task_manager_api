import asyncio
import pytest
from app.main import app, tasks
from fastapi.testclient import TestClient

@pytest.fixture(autouse=True)
def clear_tasks():
    """Ensure task storage is reset before each test"""
    tasks.clear()

@pytest.fixture
def client():
    """FastAPI test client"""
    return TestClient(app)

@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    """Globally replace asyncio.sleep with instant return to speed up tests"""
    async def instant_sleep(seconds: float):
        return None 
    monkeypatch.setattr(asyncio, "sleep", instant_sleep)