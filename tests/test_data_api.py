import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_about_me(client):
    res = client.get("/data/about_me")
    assert res.status_code == 200

def test_skills(client):
    res = client.get("/data/skills")
    assert res.status_code == 200

def test_experience(client):
    res = client.get("/data/experience")
    assert res.status_code == 200

def test_certificates(client):
    res = client.get("/data/certificates")
    assert res.status_code == 200

def test_projects(client):
    res = client.get("/data/projects")
    assert res.status_code == 200

def test_social(client):
    res = client.get("/data/social")
    assert res.status_code == 200

def test_typing(client):
    res = client.get("/data/typing")
    assert res.status_code == 200
