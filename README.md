# CSCI Final Project - Spell Checker

#### How to use

Run the `run.py` file with the following command

```bash
python run.py [mode] [input]
```

The first input is `mode` indicating whether to check file or string

1. Mode 1: Check the string
2. Mode 2: check the a `.txt` file

The second input is the string or the `.txt` file you want to check, it is either a sentence or the path to the text file.

#### Structure of project

This project composite with 3 main part:

1. A Checker 
2. A Data Structure (Dictionary)
3. Other helper functions

##### Checker

A class provides all related function to spell check, including:

1. longest common substring
2. generate candidates based on common typo
3. string checker that accepts a word to check
4. file checker that check each word in text file and save corrected version to a new file

##### Dictionary

A data structure contains necessary functions to support Checker, including:

1. ...

##### Helper function

1. run 

#### Reference 

1. [norvig.com](www.norvig.com/spell-correct.html)