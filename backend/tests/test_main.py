from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_generate_concept_map_success():
    with patch("openai.Completion.create") as mock_completion:
        mock_completion.return_value.choices[
            0
        ].text.strip.return_value = "mocked concept map"
        response = client.post("/generate_concept_map",
                               json={"prompt": "Python"})
    assert response.status_code == 200
    assert response.json() == {"concept_map": "mocked concept map"}


def test_generate_concept_map_missing_prompt():
    response = client.post("/generate_concept_map")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['body'],
                'msg': 'field required',
                'type': 'value_error.missing'
            }
        ]
    }
