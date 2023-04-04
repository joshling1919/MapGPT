from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_generate_concept_map_success():
    response = client.post("/generate_concept_map", params={"topic": "Python"})
    assert response.status_code == 200
    # Add more assertions to check the response content as needed


def test_generate_concept_map_missing_prompt():
    response = client.post("/generate_concept_map")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "topic"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
