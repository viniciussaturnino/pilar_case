from src.services import CountVowelsService


class TestCountVowelsService:
    def setup_method(self):
        self.words = ["Teste", "API", "Count", "Vowels"]
        self.service = CountVowelsService(
            words=self.words
        )

    def test_count_vowels(self):
        expected_response = {
            "Teste": 2,
            "API": 2,
            "Count": 2,
            "Vowels": 2,
        }
        result = self.service.count_vowels()

        assert result == expected_response
