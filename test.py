import sys
from src.Checker import Checker
from collections import Counter
import re

wordlist = Counter(re.findall(r'\w+', open('dict/allWords.txt').read().lower()))
chk = Checker(wordlist)
k = Checker.lcs('realisde', 'realize')
print(k)