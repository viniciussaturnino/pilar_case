from src.services import SortWordsService


class TestSortWordsService:
    def setup_method(self):
        self.words = ["Teste", "API", "Count", "Vowels"]
        self.service = SortWordsService(
            words=self.words
        )

    def test_sort_words_asc(self):
        expected_response = sorted(self.words)
        result = self.service.sort_words(order="asc")

        assert result == expected_response

    def test_sort_words_desc(self):
        expected_response = sorted(self.words, reverse=True)
        result = self.service.sort_words(order="desc")

        assert result == expected_response
