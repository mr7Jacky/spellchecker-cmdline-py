import csv
from src.HashTable import HashTable
from src.Word import Word


class HashTable2D:
    def __init__(self):
        self.size = 0
        self.hash_tables = [HashTable(20) for _ in range(26)]

    def __str__(self):
        """
        TODO - NOT WORKING
        """
        s = ''
        for i in range(len(self.hash_tables)):
            s += ("Table %s\n" % (chr(i + ord('a'))))

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
        @type ascii_sum: int
        """
        newKey = Word(key, freq)
        idx = self.__hash(key)
        self.hash_tables[idx].add(newKey)

    def search(self, target):
        idx = self.__hash(target[0])
        return self.hash_tables[idx].search(target)


def fill_hash_table(h):
    """
    @type h: HashTable2D
    """
    with open('../dict/allWords.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in readCSV:
            freq = int(''.join(row[2].split(',')))
            count += 1
            print("Insert %dth %s" % (count,row[0]))
            h.insert(row[0].lower(), freq)


if __name__ == "__main__":
    # Driver Code
    # number_of_words = size_of_table()
    # print(number_of_words)
    h = HashTable2D()  # initialize the hash table
    h.insert("haha",1)
    h.insert("ahah",2)
    h.insert("hehe",3)
    h.insert("hahz",4)
    h.insert('b',5)
    print(h)
    print(h.search('hahz'))
    print(h.search('a'))
