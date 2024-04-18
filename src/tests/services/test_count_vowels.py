from src.services import CountVowelsService


class TestCountVowelsService:
    def setup_method(self):
        self.words = []
        self.service = CountVowelsService(
            words=self.words
        )

    def test_count_vowels(self):
        result = self.service.count_vowels()

        assert result == len(self.words)
