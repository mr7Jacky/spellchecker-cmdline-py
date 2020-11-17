from src.Word import Word


class HashTable:
    """
    Modified hash table, designing for hash words
    The hash function is based on the sum of ASCII for each word
    """

    def __init__(self, length=5):
        """
        Initialization function of the hashtable, where:
            maxLoad is the the maximum load value the HashMap can reach before possibly resizing
            array is the array to store items
            capacity if the total number of arrays it has
            max_load max load to resize
            array_load number of none empty array
            num_item total items in table
        @param length: initial capacity of hash table
        @type length: int
        """
        self.array = [[] for _ in range(length)]
        self.capacity = length
        self.max_load = 0.75
        self.array_load = 0
        self.num_items = 0

    def size(self):
        """
        Get the number of items in hash table
        @rtype: int
        @return: the number of items in hash table
        """
        return self.num_items

    def is_empty(self):
        """
        Check if the hash table is empty
        @rtype: bool
        @return: True if empty else False
        """
        return self.size() == 0

    def search(self, target):
        """
        Search in the hash table and check if it is in the hash table
        @type target: str
        @param target: the target to compare with
        @rtype: Word
        @return: Return a Word object of the target if found else None
        """
        index = self.hash(target)
        for i in self.array[index]:
            if i.word == target:
                return i
        return None

    def hash(self, word):
        """
        Convert a string into a position index in the hashtable
        Based on the sum of ASCII - encoding
        @type word: str
        @param word: word to convert
        @rtype: int
        @return: the index in the hashtable
        """
        ascii_sum = 0
        for i in range(int(len(word) / 2) + 1):
            ascii_sum += ord(word[i]) - ord('a')
        return ascii_sum % self.capacity

    def __contains__(self, item):
        """
        Check if an item is in the hashtable
        @type item: str
        @param item: the item to check
        @rtype: bool
        @return: return if the item is in the array
        """
        return self.search(item) is not None

    def add(self, key):
        """
        Add the key to the hash table
        @type key: Word
        @param key: the key added to the hash table
        """
        if not self.search(key.word):
            index = self.hash(key.word)
            if len(self.array[index]) == 0:
                self.array_load += 1
            self.array[index].append(key)
            self.num_items += 1
            load_factor = self.array_load / self.capacity  # Calculate current load factor
            if load_factor > self.max_load:
                self.resize()

    def resize(self):
        """
        Resize the hashtable; extend to a larger hash table
        """
        self.capacity *= 2
        newArray = [[] for _ in range(self.capacity)]
        for i in self.array:
            if len(i) != 0:
                for j in i:
                    index = self.hash(j.word)
                    newArray[index].append(j)
        self.array = newArray

    def __str__(self):
        """
        Get the string representation of the hashtable
        @rtype: str
        @return: the string representation of the hashtable
        """
        s = ''
        for i in range(len(self.array)):
            s += str(i) + ' '
            for j in self.array[i]:
                s += '--> ' + j.word + ' '
            s += '\n'
        return s[:-1]

    def __repr__(self):
        """
        Get the string representation of the hashtable
        @rtype: str
        @return: the string representation of the hashtable
        """
        s = ''
        for i in range(len(self.array)):
            s += str(i) + ' '
            for j in self.array[i]:
                s += '--> ' + j.word + ' '
            s += '\n'
        return s


if __name__ == "__main__":
    h = HashTable()
    h.add(Word("haha", 1))
    h.add(Word("ahah", 2))
    h.add(Word("hehe", 3))
    h.add(Word("hahz", 4))
    h.add(Word('b', 5))
    print(h)
    print("hoho" in h)
