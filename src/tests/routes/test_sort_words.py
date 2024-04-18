from fastapi.testclient import TestClient
from main import app


class TestSortWords:
    def setup_method(self):
        self.client = TestClient(app)
        self.words = ["Teste", "API", "Count", "Vowels"]
        self.data = {
            "words": self.words,
            "order": "asc"
        }

    def test_sort_words(self):
        expected_response = sorted(self.words)

        response = self.client.post("/sort-words", json=self.data)

        assert response.status_code == 200
        assert response.json() == expected_response
