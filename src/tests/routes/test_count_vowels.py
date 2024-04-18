from fastapi.testclient import TestClient
from main import app


class TestCountVowels:
    def setup_method(self):
        self.client = TestClient(app)
        self.words = ["Teste", "API", "Count", "Vowels"]
        self.data = {
            "words": self.words
        }

    def test_count_vowels(self):
        expected_response = {
            "Teste": 2,
            "API": 2,
            "Count": 2,
            "Vowels": 2,
        }

        response = self.client.post("/count-vowels", json=self.data)

        assert response.status_code == 200
        assert response.json() == expected_response
