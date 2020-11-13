class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word
