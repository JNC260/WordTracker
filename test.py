import functions
from matplotlib import pyplot as plt 

text = "I would like to acknowledge that I like an elephant a lot.  My favorite land animal is the elephant because the elephant is a large and gentle creature that feels like humans do.  I wish I could ride an elephant."

words = functions.formatInputText(text)

#print(words)

counts = functions.findWordCount(words)

#print(counts)

most = functions.findMostUsed(counts)

#print(most)

bar = functions.wordBarGraph(counts, words)

plt.show(bar)

pie = functions.wordPieChart(counts, words)

#plt.show(pie)