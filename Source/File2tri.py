# Needed library
from nltk.collocations import ngrams
from nltk.tokenize import word_tokenize
# reading the file
infile = open('input.txt','r', encoding="utf-8")

# Giving the file a neame
text = infile.read()
# Using the word_tokenize library
words = word_tokenize(text)
# here we are telling it ti be a tri gram
X = ngrams(words, 3)

# this loop is needed so that it will read output all the trigrams
for a in X:
    print(a)
