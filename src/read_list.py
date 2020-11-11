words_list = []
with open("wordlist.txt", "r") as f:
    words_list = f.readlines()
words_list = [x.strip() for x in words_list]
for x in range(len(words_list)):
    print(words_list[x])
