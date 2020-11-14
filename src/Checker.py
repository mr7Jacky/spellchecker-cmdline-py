import sys
from src.HashTable2D import HashTable2D


class Checker:
    """ Checker class provides helper function to check the spelling"""

    def __init__(self, wordlist, num_candidates=5):
        """ Initialize function for Checker class
        @type wordlist: HashTable2D
        @param wordlist: a dictionary contains all available words
        @type num_candidates: int
        @param num_candidates: the number of candidates to generate
        """
        self.wordlist = wordlist
        self.num_candidates = num_candidates

    def str_checker(self, str_in):
        """ Check the spelling for given string, if not in wordlist, find the similar ones
        @type str_in: str
        @param str_in: target string to check
        @rtype: list
        @return: a list of possible string
        """
        if str_in in self.wordlist:
            return [str_in]
        possible_words = Checker.generate_possible_words(str_in)
        candidates = self.linear_search(possible_words, str_in, self.num_candidates)
        if len(candidates) == 0:
            candidates = self.linear_search(self.wordlist.get_elements(), str_in, self.num_candidates)
        return candidates

    def file_checker(self, path):
        """ Check the spelling for each word in given file, if not in wordlist, find the similar ones

        It will generate a new corrected spelling file in the same directory provided.
        @type path: str
        @param path: path to the file
        """
        # add progress bar
        toolbar_width = 50
        count = 0
        # setup toolbar
        sys.stdout.write("%6.2f%%|%s|" % (0, (" " * toolbar_width)))
        sys.stdout.flush()

        # correct spelling
        file_name = path.split('.')[0]
        with open(path, 'r') as src_file, open(f'{file_name}_cort.txt', 'w+') as corrected_file:
            lines = src_file.readlines()
            for line in lines:
                line = self.split_helper(line, 0)
                # update the bar
                count += 1
                sys.stdout.write('\r')
                percent = float(count / len(lines))
                sys.stdout.write("%6.2f%%|%s>" % (percent * 100, ("=" * int(percent * 50))))
                sys.stdout.flush()
                # write to the end of line
                corrected_file.write(line)
                corrected_file.write('\n')
            sys.stdout.write("|\n")  # this ends the progress bar ■

    def split_helper(self, in_str, split_index):
        """ Helper function to split sentence by sentence and comma by comma
        @type in_str: str
        @param in_str: string to split
        @type split_index: int
        @param split_index: use to choose level of split (sentence or comma or word)
        """
        split_order = ['.', ',', '']
        ret = ''
        delimiter = split_order[split_index]
        if delimiter == '':
            strings = in_str.split()
        else:
            strings = in_str.split(delimiter)
        for i in range(len(strings)):
            string = strings[i]
            if split_index == (len(split_order) - 1):
                # word mode
                lowered_word = string.lower()
                replaced_word = self.str_checker(lowered_word)[0]
                if lowered_word[0] != string[0]:
                    # check if capitalized
                    replaced_word = replaced_word.capitalize()
                ret += replaced_word
            else:
                ret += self.split_helper(string, split_index + 1)
            if len(strings)-1 == i:
                break
            ret += split_order[split_index] + ' '
        return ret

    def linear_search(self, search_area, target, num_candidates):
        """ Linearly search the target within the given set based on lcs
        @type search_area: set
        @param search_area: set of words we compare to target
        @type target: str
        @param target: the string to compare
        @type num_candidates: int
        @param num_candidates: top n number words will be return
        @rtype: list
        @return: a number indicating the number of common characters in both input strings
        """
        candidates = [word for word in search_area if word in self.wordlist]
        # get top n candidates based on lcs score
        self.merge_sort_lcs(candidates, 0, len(candidates)-1, target)
        ret = list(candidates)[0:num_candidates]
        return ret

    def merge_sort_lcs(self, arr, left, right, target):
        if left < right:
            m = (left + (right - 1)) // 2
            self.merge_sort_lcs(arr, left, m, target)
            self.merge_sort_lcs(arr, m + 1, right, target)
            self.__merge_lcs(arr, left, m, right, target)

    def __merge_lcs(self, arr, left, mid, right, target):
        n1 = mid - left + 1
        n2 = right - mid
        # create temp arrays
        L = [0] * n1
        R = [0] * n2
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[left + i]
        for j in range(0, n2):
            R[j] = arr[mid + 1 + j]
        # Merge the temp arrays back into arr[left..right]
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if Checker.lcs(target, L[i]) > Checker.lcs(target, R[j]):
                arr[k] = L[i]
                i += 1
            else:
                if self.wordlist.search(L[i]).freq >= self.wordlist.search(R[i]).freq:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    @staticmethod
    def lcs(first_str, second_str) -> int:
        """ Function to check the longest common subsequence of two string

        Dynamic programming button-up version of longest common subsequence
        runtime O(mn)
        where:
            mid is the length of first string
            n is the length of second string
        @type first_str: str
        @param first_str: the first string to compare
        @type second_str: str
        @param second_str: the first string to compare
        @rtype: int
        @return: a number indicating the number of common characters in both input strings
        """
        m = len(first_str)
        n = len(second_str)
        C = [[0] * (n + 1)] * (m + 1)

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    C[i][j] = 0
                elif first_str[i - 1] == second_str[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                else:
                    C[i][j] = max(C[i - 1][j], C[i][j - 1])

        return C[m][n]

    @staticmethod
    def generate_possible_words(word):
        """ Function to create all possible words of given word based on common mistakes
        @type word: str
        @param word: the first string to compare
        @rtype: set
        @return: a set of all possible words related to given word
        """
        return Checker.__one_letter_diff(word).union(Checker.__two_letter_diff(word))

    @staticmethod
    def __one_letter_diff(word):
        """ Generate all words that is one letter different from word
        @type word: str
        @param word: the input word
        @rtype: set
        @return: a set of words with one letter differing from input word
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        surround_letter = {'q': 'wa', 'w': 'qase', 'e': 'wsdr', 'r': 'etdf', 't': 'rfgy', 'y': 'tghu', 'u': 'yjhi',
                           'i': 'uko', 'o': 'ilkp', 'p': 'ol', 'a': 'sqwz', 's': 'waxzd', 'd': 'serfcx', 'f': 'rtgdvc',
                           'g': 'ftyvhb', 'h': 'gyujnb', 'j': 'huiknm', 'k': 'jiolm', 'l': 'pok',
                           'z': 'axs', 'x': 'zcsd', 'c': 'xdfv', 'v': 'cfgb', 'b': 'vghn', 'n': 'bhjm', 'm': 'njk'}
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        # replace by the near by target
        replaces = [L + c + R[1:] for L, R in splits if R for c in surround_letter.get(R[0])]
        # replace by all letter
        # replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]

        return set(deletes + transposes + replaces + inserts)

    @staticmethod
    def __two_letter_diff(word):
        """ Generate all words that is two letter different from word
        @type word: str
        @param word: the input word
        @rtype: set
        @return: a set of words with 2 letter differing from input word
        """
        return set(e2 for e1 in Checker.__one_letter_diff(word) for e2 in Checker.__one_letter_diff(e1))
