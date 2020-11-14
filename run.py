import sys
from src.Checker import Checker
from src.HashTable2D import HashTable2D
from os import path
import pickle


def print_instruction():
    print("Usage: run.py [mode] [input]")
    print("Parameter [mode] can be either 1 for string or 2 for text file.")
    print("If mode is 1, enter the string in [input].")
    print("If mode is 2, enter the path to [input] text file.")


def store_data():
    wordlist = HashTable2D()
    wordlist.fill_hash_table('./dict/allWords.csv')
    # Its important to use binary mode
    file = open('dict/dictionary', 'ab')
    # source, destination
    pickle.dump(wordlist, file)
    file.close()


def load_data():
    # for reading also binary mode is important
    file = open('dict/dictionary', 'rb')
    return pickle.load(file)


def main():
    if len(sys.argv) != 3:
        print_instruction()
        sys.exit()
    # test word list
    if not path.exists("dict/dictionary"):
        store_data()
    wordlist = load_data()
    chk = Checker(wordlist)
    in_type = int(sys.argv[1])
    usr_in = sys.argv[2]
    if in_type == 1:
        usr_in = usr_in.split()
        for word in usr_in:
            cor_str = chk.str_checker(word.lower())
            print("Correction %s --> %s" % (word, cor_str[0]))
            print("Other candidates: %s" % cor_str)
    elif in_type == 2:
        chk.file_checker(usr_in)
        print("Saving corrected file to %s_cort.txt" % (usr_in[:-4]))
    else:
        print("Error: Invalid Type.")
        print_instruction()


if __name__ == "__main__":
    main()
