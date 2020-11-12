def size_of_table():
    f = open("../dict/allWords.txt", "r")
    number_of_words = 0
    for line in f:
        number_of_words += 1
    return number_of_words


def fill_hash_table():
    f = open("../dict/allWords.txt", "r")
    for line in f:
        line = line.strip()
        ascii_sum = 0
        for i in range(0, int(len(line) / 2) + 1):
            ascii_sum += ord(line[i])
        # print(ascii_sum)
        insert(ascii_sum, line)
        # print(len(words_list))
    # for x in range(len(words_list)):
    # print(words_list[x])


def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

    # Hashing Function to return


# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)


# Insert Function to add 
# values to the hash table 
def insert(keyvalue, value):
    hash_key = Hashing(keyvalue)
    HashTable[hash_key].append(value)


# Driver Code
number_of_words = size_of_table()
# print(number_of_words)
HashTable = [[] for _ in range(number_of_words)]  # initialize the hash table
fill_hash_table()
display_hash(HashTable)
