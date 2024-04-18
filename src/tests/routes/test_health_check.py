from fastapi.testclient import TestClient
from main import app


class TestHealthCheck:
    client = TestClient(app)

    def test_index(self):
        expected_response = {"message": "Hello, World!"}
        response = self.client.get("/health_check/")
        assert response.status_code == 200
        assert response.json() == expected_response
