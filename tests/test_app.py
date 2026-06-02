import json
import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_valid_question_returns_200(client):
    response = client.post(
        "/ask",
        data=json.dumps({"question": "How do I track my shipment?"}),
        content_type="application/json",
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "answer" in data
    assert "sources" in data


def test_missing_question_returns_400(client):
    response = client.post(
        "/ask",
        data=json.dumps({"note": "no question here"}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_blank_question_returns_400(client):
    response = client.post(
        "/ask",
        data=json.dumps({"question": "   "}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
