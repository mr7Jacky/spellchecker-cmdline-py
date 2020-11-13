from src.Word import Word


class HashTable:
    def __init__(self, length=5):
        """maxLoad is the the maximum load value the HashMap can reach
        before possibly resizing"""
        self.array = [[] for _ in range(length)]
        self.capacity = length
        self.maxLoad = 0.75
        self.array_load = 0
        self.numItems = 0
        self.iter_ptr = 0

    def size(self):
        return self.numItems

    def is_empty(self):
        return self.size() == 0

    def search(self, target):
        """
        @type target: str
        """
        index = self.hash(target)
        for i in self.array[index]:
            if i.word == target:
                return i
        return None

    def hash(self, word):
        """
        @type word: str
        """
        ascii_sum = 0
        for i in range(0, int(len(word) / 2) + 1):
            ascii_sum += ord(word[i]) - ord('a')
        return ascii_sum % self.capacity

    def __contains__(self, item):
        return self.search(item) is not None

    def add(self, key):
        """
        @type key: Word
        """
        if not self.search(key.word):
            index = self.hash(key.word)
            if len(self.array[index]) == 0:
                self.array_load += 1
            self.array[index].append(key)
            self.numItems += 1
            loadFactor = self.array_load / self.capacity  # Calculate current load factor
            if loadFactor > self.maxLoad:
                self.resize()

    def resize(self):
        self.capacity *= 2
        newArray = [[] for _ in range(self.capacity)]
        for i in self.array:
            if len(i) != 0:
                for j in i:
                    index = self.hash(j.word)
                    newArray[index].append(j)
        self.array = newArray

    def __str__(self):
        s = ''
        for i in range(len(self.array)):
            s += str(i) + ' '
            for j in self.array[i]:
                s += '--> ' + j.word + ' '
            s += '\n'
        return s[:-1]

    def __repr__(self):
        s = ''
        for i in range(len(self.array)):
            s += str(i) + ' '
            for j in self.array[i]:
                s += '--> ' + j.word + ' '
            s += '\n'
        return s





if __name__ == "__main__":
    h = HashTable()
    h.add(Word("haha",1))
    h.add(Word("ahah",2))
    h.add(Word("hehe",3))
    h.add(Word("hahz",4))
    h.add(Word('b',5))
    print(h)
    print("hoho" in h)
