import csv
from src.HashTable import HashTable
from src.Word import Word
import os.path


class HashTable2D:
    """
    An advanced data structure of Hash Table, where it contains a list of hash tables (26),
    each represent a wordlist for all words start with the same letter
    """

    def __init__(self):
        """
        Initialization of 2D hash table:
            size: is the number of elements in the hashtable
            hash_tables: a list of hashtable as word lists
            elements: store all the words
        """
        self.size = 0
        self.hash_tables = [HashTable(20) for _ in range(26)]
        self.elements = set()

    def __str__(self):
        """
        Get the string representation of the 2d hashtable
        @rtype: str
        @return: the string representation of the 2d hashtable
        """
        s = ''
        for i in range(len(self.hash_tables)):
            s += ("Table %s\n" % (chr(i + ord('a'))))
            s += str(self.hash_tables[i])
        return s

    @staticmethod
    def __hash(key):
        """
        Convert a string into a position index in the hashtable
        Based on the sum of ASCII - encoding
        @type key: str
        @param key: word to convert
        @rtype: int
        @return: the index in the hashtable
        """
        return ord(key[0]) - ord('a')

    def insert(self, key, freq):
        """
        Add the Word to hash table with given word and frequency
        @type key: str
        @param key: the word to add
        @type freq: int
        @param: the frequency of that word
        """
        newKey = Word(key, freq)
        idx = self.__hash(key)
        self.size += 1
        self.hash_tables[idx].add(newKey)

    def search(self, target):
        """
        Search in the hash table and check if it is in the hash table
        @type target: str
        @param target: the target to compare with
        @rtype: Word
        @return: Return a Word object of the target if found else None
        """
        if target == '':
            return None
        idx = self.__hash(target[0])
        return self.hash_tables[idx].search(target)

    def __contains__(self, item):
        """
        Check if an item is in the hashtable
        @type item: str
        @param item: the item to check
        @rtype: bool
        @return: return if the item is in the array
        """
        return self.search(item) is not None

    def get_elements(self):
        """
        Get all the elements in the hash table
        @rtype: set
        @return: a set contains all the elements in the hash table
        """
        return self.elements

    def fill_hash_table(self, file_name):
        """
        Read from given file path to create a wordlist as a HashTable2D object
        @type file_name: str
        @param file_name: the path to the file
        """
        if not os.path.exists(file_name):
            print("FAIL TO OPEN THE FILE")
            exit(-1)
        with open(file_name) as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            count = 0
            for row in readCSV:
                freq = int(''.join(row[2].split(',')))
                count += 1
                print("%dth insert %s" % (count, row[0]))
                self.insert(row[0].lower(), freq)
                self.elements.add(row[0].lower())


if __name__ == "__main__":
    h = HashTable2D()
    h.fill_hash_table('../dict/allWords.csv')
    print(h)
