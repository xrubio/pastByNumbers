      

def getFrequent(freqs, numFrequentWords):
    sortedWords = sorted(freqs, key=freqs.get, reverse=True)
    mostFrequent = sortedWords[0:numFrequentWords]
    listFreqs = []
    for word in mostFrequent:
        listFreqs.append(freqs[word])
    return mostFrequent,listFreqs

def getWords(bookFile):

    # create empty list
    listOfWords = []
    book = open(bookFile)

    for line in book:
        splitLine = line.split()
        for word in splitLine:
            listOfWords.append(word)
    print("number of words:",len(listOfWords))
    return listOfWords
    
def countWords(listOfWords):
    # create an empty dictionary
    uniqueWords = {}    
    for word in listOfWords:
        if word in uniqueWords:
            uniqueWords[word] = uniqueWords[word]+1
        else:
            uniqueWords[word] = 1
    print("number of unique words:",len(uniqueWords))
    return uniqueWords            
       
# parameters
bookFile = "../books/frankenstein.txt"

# top 50 frequent words
numFrequentWords = 40
print("counting the top",numFrequentWords,"from book:",bookFile)

# split the book in words and count them
wordList = getWords(bookFile)
freqs = countWords(wordList)

# select and print the most frequent ones
topWords,topFreqs = getFrequent(freqs,numFrequentWords)
print(numFrequentWords," most frequent words are:",topWords,"with freqs:",topFreqs)

import matplotlib.pyplot as plt

plt.plot(range(len(topWords)), topFreqs, "o")
plt.xticks(range(len(topWords)), topWords, rotation=45)
plt.show()
