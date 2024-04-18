class CountVowelsService:
    def __init__(self, words):
        self.words = words
        self.vowels = "aeiou"

    def count_vowels(self) -> dict:
        response = {}

        for word in self.words:
            count = sum(1 for c in word.lower() if c in self.vowels)
            response[word] = count

        return response
