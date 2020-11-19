# CSCI 311 Final Project - Spell Checker

## How to use

Run the `run.py` file with the following command

```bash
python run.py [mode] [input]
```

The first input is `mode` indicating whether to check file or string

1. Mode 1: Check the string
2. Mode 2: check the a `.txt` file

The second input is the string or the `.txt` file you want to check, it is either a sentence or the path to the text file.

## Structure of project and Runtime
#### [Full version Report](doc/Report.pdf)

This project composite with 3 main parts:

1. A Checker 
2. A Data Structure (Dictionary)
3. Other helper functions

#### [Checker](src/Checker.py)

A class provides all related function to spell check, including:

1. longest common substring that scores the similarity between target word the word to compare
2. merge sort that sorts the candidates of target words based on lcs score and frequency of the word
2. generate candidates based on common typo 
3. string checker that accepts a word to check and returns the top choice and some candidates
4. file checker that checks each word in text file, replaces with the top choice of candidates, save corrected version to a new file

#### Dictionary

##### [2D Hash Table](src/HashTable2D.py)
Basically, this data structure consists of 26 small hash tables. Within each hash table, the first letter of words stored is the same. So the hash function is determined by the leading letter of each input word. Other method, including search and insert are all based on the following small basic hash table

##### [Hash Table](src/HashTable.py)
This hash table is very similar to the regular hash table, but we modify the hash function so that it is customized for the use of words in this program. We implemented based on the sum of ASCII encoding for each letter in input word. 

Additionally, this hash table will extend dynamically according to the number of empty array remaining in the hash table. If the number decreases over threshold (default = 0.25), then the hash table will double its size and redistribute the element in it. In this way:

 1. We prevent there is too many item in the save location of the hash table, which will increase the cost of search function. 
 2. We can void there is too many empty location in it.

#### Helper function

We use [run.py](run.py) to trigger the program; It does the following things:
1. (First time use) Read from file, create a wordlist, and save it locally
2. Load the wordlist from previously save file
3. Accept user input argument 
4. Start checker

## Reference 

1. [Norvig](https://www.norvig.com/spell-correct.html)
2. [Academic Words](https://www.academicwords.info/)
