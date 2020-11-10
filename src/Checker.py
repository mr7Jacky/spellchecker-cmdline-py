class Checker:
	""" Checker class provides helper function to check the spelling"""
	def __init__(self, wordlist):
		""" Initialize function for Checker class
		@type wordlist: HashTable
		@param first_str: a dictionary contains all available words
		"""
		self.wordlist = wordlist
		self.num_candidates = 5;

	@classmethod
	def str_checker(self, str_in):
		""" Check the spelling for given string, if not in wordlist, find the similar ones
		@type str_in: str
		@param str_in: target string to check
		@rtype: set
		@return: a set of possible string
		"""
		if str_in in self.wordlist:
			return set(str_in)
		possible_words = generate_possible_words(str_in)
		candidates = self.linear_search(possible_words, str_in, self.num_candidates)
		return candidates


	@classmethod
	def file_checker(self, usr_in):
		""" Function to check the longest common subsequence of two string

		Dynamic programming buttom-up version of longest common subsequence
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
		pass

	@classmethod
	def linear_search(self, searchArea, target, maxRet):
		""" Linearly search the target within the given set based on lcs
		@type searchArea: set
		@param searchArea: set of words we compare to target
		@type target: str
		@param target: the string to compare
		@type maxRet: int
		@param maxRet: top n number words will be return
		@rtype: set
		@return: a number indicating the number of common characters in both input strings
		"""
		#TODO
		pass

	@staticmethod
	def lcs(first_str, second_str) -> int:
		""" Function to check the longest common subsequence of two string

		Dynamic programming buttom-up version of longest common subsequence
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
		# find the length of the strings 
		m = len(first_str)
		n = len(second_str)
	  
		# declaring the array for storing the dp values 
		C = [[None]*(n+1) for i in range(m+1)]
	  
		# Buttom up
		for i in range(m+1): 
		    for j in range(n+1): 
		        if i == 0 or j == 0 : 
		            C[i][j] = 0
		        elif first_str[i - 1] == second_str[j - 1]:
		            C[i][j] = C[i-1][j-1]+1
		        else: 
		            C[i][j] = max(C[i-1][j] , C[i][j-1])
	  
		# L[m][n] contains the length of LCS
		return C[m][n]

	@staticmethod
	def generate_possible_words(word):
		""" Function to create a set of all possible words of given word based on common mistakes
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