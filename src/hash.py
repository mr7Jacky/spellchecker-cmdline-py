class HashTable:
    def __init__(self, length = 5):
        """maxLoad is the the maximum load value the HashMap can reach
        before possibly resizing"""
        self.array = [None] * length
        self.capacity = length
        self.maxLoad = 0.75
        self.numItems = 0

    def size(self):
        return self.numItems

    def isEmpty(self):
        return self.size() == 0
    
    def hash(self, key):
        return hash(key) % self.capacity

    def search(self, key):
        index = self.hash(key)
        if self.array[index] is not None:
            for i in range(len(self.array[index])):
                if self.array[index][i] == key:
                    return True
        return False
        
    def add(self, key):
        if not self.search(key):
            index = self.hash(key)
            if self.array[index] == None:
                self.array[index] = [key]
            else:
                self.array[index].append(key)
            self.numItems += 1
            loadFactor = self.numItems / self.capacity #Calculate current load factor
            if loadFactor > self.maxLoad:
                self.resize()

    def resize(self):
        print("resizing")
        self.capacity *= 2
        newArray = [None] * self.capacity
        for i in range(len(self.array)):
            if self.array[i] is not None:
                for j in range(len(self.array[i])):
                    index = self.hash(self.array[i][j])
                    if newArray[index] is None:
                        newArray[index] = [self.array[i][j]]
                    else:
                        newArray[index].append(self.array[i][j])
        self.array = newArray

    def displayHashTable(self):
        for i in range(len(self.array)):
            if self.array[i] is not None:
                print(i, end = " ")
                for j in self.array[i]:
                    print("-->", end = " ")
                    print(j, end = " ")
                print()


something = HashTable()
something.add("haha")
something.add("ahah")
something.add("hehe")
something.add("hahz")
print(something.search("haha"))
print(something.search("hoho"))
something.displayHashTable()
        
            
        
        
            
