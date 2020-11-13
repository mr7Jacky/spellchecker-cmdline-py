import csv
from src.HashTable import HashTable
from src.Word import Word


class HashTable2D:
    def __init__(self):
        self.size = 0
        self.hash_tables = [HashTable(20) for _ in range(26)]

    def __str__(self):
        s = ''
        for i in range(len(self.hash_tables)):
            s += ("Table %s\n" % (chr(i + ord('a'))))
            s += i.__str__()
        return s

    # target for every value.
    @staticmethod
    def __hash(key):
        """
        @type key: Word
        """
        return ord(key.word[0]) - ord('a')

    # Insert Function to add
    # values to the hash table
    def insert(self, key, freq):
        """
        @type key: str
        @type freq: int
        @type ascii_sum: int
        """
        newKey = Word(key, freq)
        idx = self.__hash(newKey)
        self.hash_tables[idx].add(newKey)

    def search(self, target):
        idx = self.__hash(target[0])
        return self.hash_tables[idx].search(target)


def fill_hash_table(h):
    with open('dict/allWords.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            ascii_sum = 0
            freq = int(''.join(row[2].split(',')))
            for i in range(0, int(len(row[0]) / 2) + 1):
                ascii_sum += ord(row[0][i])
            # insert(ascii_sum, (row[0].lower(), freq, ascii_sum))


if __name__ == "__main__":
    # Driver Code
    # number_of_words = size_of_table()
    # print(number_of_words)
    h = HashTable2D()  # initialize the hash table
    print(h)
