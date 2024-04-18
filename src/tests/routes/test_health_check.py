from fastapi.testclient import TestClient
from main import app


class TestHealthCheck:
    def setup_method(self):
        self.client = TestClient(app)

    def test_index(self):
        expected_response = {"message": "Hello, World!"}
        response = self.client.get("/health_check/")
        assert response.status_code == 200
        assert response.json() == expected_response
