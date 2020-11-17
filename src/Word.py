class Word:
    """
    Class represent a word
    """

    def __init__(self, word, freq):
        """ Initialization function for class
        @type word: str
        @param word: word
        @type freq: int
        @param freq: the frequency of the word
        """
        self.word = word
        self.freq = freq

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word
