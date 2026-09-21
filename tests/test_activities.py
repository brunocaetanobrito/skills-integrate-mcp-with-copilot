import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app


client = TestClient(app)


def test_github_skills_activity_is_available():
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert "GitHub Skills" in activities
    assert activities["GitHub Skills"]["description"]
    assert activities["GitHub Skills"]["participants"] == []
