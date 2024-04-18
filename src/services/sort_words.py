from typing import List

from ..schemas import SortOrderEnum


class SortWordsService:
    def __init__(self, words: List[str]):
        self.words = words

    def sort_words(self, order: str) -> List[str]:
        if order == SortOrderEnum.ASC:
            return sorted(self.words)
        else:
            return sorted(self.words, reverse=True)
