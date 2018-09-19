import re
from matplotlib import pyplot as plt 
from matplotlib import style

def formatText(file){
    text = open(file)
    words = text.split(" ")
    return words
}

