import csv
from src.HashTable import HashTable
from src.Word import Word
import os.path


class HashTable2D:
    def __init__(self):
        self.size = 0
        self.hash_tables = [HashTable(20) for _ in range(26)]
        self.elements = set()

    def __str__(self):
        s = ''
        for i in range(len(self.hash_tables)):
            s += ("Table %s\n" % (chr(i + ord('a'))))
            s += str(self.hash_tables[i])
        return s

    # target for every value.
    @staticmethod
    def __hash(key):
        """
        @type key: str
        """
        return ord(key[0]) - ord('a')

    # Insert Function to add
    # values to the hash table
    def insert(self, key, freq):
        """
        @type key: str
        @type freq: int
        """
        newKey = Word(key, freq)
        idx = self.__hash(key)
        self.size += 1
        self.hash_tables[idx].add(newKey)

    def search(self, target):
        """
        @rtype : Word
        """
        idx = self.__hash(target[0])
        return self.hash_tables[idx].search(target)

    def __contains__(self, item):
        return self.search(item) is not None

    def get_elements(self):
        return self.elements

    def fill_hash_table(self, file_name):
        """
        @type file_name: str
        """
        if not os.path.exists(file_name):
            print("FAIL TO OPEN THE FILE")
            exit(-1)
        with open(file_name) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            count = 0
            for row in readCSV:
                freq = int(''.join(row[2].split(',')))
                count += 1
                print("%dth insert %s" % (count, row[0]))
                self.insert(row[0].lower(), freq)
                self.elements.add(row[0].lower)


if __name__ == "__main__":
    # Driver Code
    # number_of_words = size_of_table()
    # print(number_of_words)
    h = HashTable2D()  # initialize the hash table
    h.fill_hash_table('../dict/allWords.csv')
    print(h)
