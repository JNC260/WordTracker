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

    return wordList

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

    return wordList        

#build dictionary with word list with counts
def findWordCount(list):

    wordCount = {} #initialize empty dictionary, keys will be words, values will be the count

    for word in list:
        if word not in wordCount:
            wordCount[word] = 1 #add to dictionary and set count to 1
        else:
            wordCount[word] = wordCount[word] + 1 #if its there, increase the count by one

    return wordCount

#find most used word and its count from a dictonary of words and counts and a list of words
def findMostUsed(dict):

    largestCount = 0 #initalize count and word used most
    most = ""
   
    for word, count in dict.items():
        if count > largestCount: #change the word and count when a larger count is encountered
            most = word
            largestCount = count

    return "The word used the most in this text is "+word+". It was used "+count+" times."

#use word list and dictionary to create a bar graph
def wordBarGraph(dict, list):
    x = [] #initalize x and y values
    y = []
    minCount = round(len(list)*0.01) #filters out words used less than one percent of total word count (i.e: for 100 words, words used more than once)
    
    for word, count in dict.items():
        if count > minCount:
            x.append(word) #add word to x values
            y.append(count) #and count to y values
    
    wordBar = plt.bar(x,y) #create bar graph
    plt.title('Word Usage')
    plt.xlabel('Words')
    plt.xticks(rotation=90)
    plt.ylabel('Frequency')
    
    return wordBar


def wordPieChart(dict, list):
    
    labels = [] #initalize labels and values
    values = []
    minCount = round(len(list)*0.01) #filters out words used less than one percent of total word count (i.e: for 100 words, words used more than once)
    
    for word, count in dict.items():
        if count > minCount:
            labels.append(word) #add word to labels
            values.append(count) #and count to values

    wordPie = ply.pie(values, labels=labels)

    return wordPie
