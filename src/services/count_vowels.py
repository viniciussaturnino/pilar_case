class CountVowelsService:
    def __init__(self, words):
        self.words = words

    def count_vowels(self):
        return len(self.words)
