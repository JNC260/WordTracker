import re
from matplotlib import pyplot as plt 
from matplotlib import style

exceptions = {
    "the": 1, "be": 2, "to": 3, "of": 4, "and": 5,
    "a": 6, "in": 7, "that": 8, "have": 9, "i": 10,
    "it": 11, "for": 12, "not": 13, "on": 14, "with": 15
}

#format words from a file
def formatFileText(file):
    text = open(file, 'r').read() #read text in the file
    words = text.split(" ") #split text into list of words
    wordList = [] #initialize a new list
    for word in words:
        lower = word.lower() #make all words lowercase for more accurate counting
        if lower in exceptions: #dont count top 15 most common words
            wordList = wordList
        else:
            fixedWord = re.findall(r'[a-z]*', lower) #filter out punctuation or whitespace, returns a list with a length of 1
            wordList.append(fixedWord[0]) #add item in list to the wordList    

#format words from text input
def formatInputText(text):
    words = text.split(" ")
    wordList = []
    for word in words:
        lower = word.lower() #make all words lowercase for more accurate counting
        if lower in exceptions: #dont count top 15 most common words
            wordList = wordList
        else:
            fixedWord = re.findall(r'[a-z]*', lower) #filter out punctuation or whitespace, returns a list with a length of 1
            wordList.append(fixedWord[0]) #add item in list to the wordList      


