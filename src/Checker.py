class Checker:
    """ Checker class provides helper function to check the spelling"""

    def __init__(self, wordlist, num_candidates=5):
        """ Initialize function for Checker class
        @type wordlist: HashTable
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
            candidates = self.linear_search(self.wordlist,str_in, self.num_candidates)
        return candidates

    def file_checker(self, path):
        """ Check the spelling for each word in given file, if not in wordlist, find the similar ones

        It will generate a new corrected spelling file in the same directory provided.
        @type path: str
        @param path: path to the file
        """
        with open(path, 'r') as src_file, open('s_cort.txt', 'w+') as corrected_file:
            for line in src_file:
                for word in line.split():
                    print(self.str_checker(word))
                    line = line.replace(word, self.str_checker(word)[0])
                corrected_file.write(line)

        

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
        candidates = set(word for word in search_area if word in self.wordlist)
        # get top n candidates based on lcs score
        sorted(candidates, key=lambda x: Checker.lcs(x, target)) # TODO - Use Mergesort instead of build-in sorted
        ret = list(candidates)[0:num_candidates]
        return ret

    @staticmethod
    def lcs(first_str, second_str) -> int:
        """ Function to check the longest common subsequence of two string

        Dynamic programming button-up version of longest common subsequence
        runtime O(mn)
        where:
            m is the length of first string
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
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)
