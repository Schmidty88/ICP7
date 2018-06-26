# Needed library
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
file = open('input.txt', 'r', encoding="utf-8")

# setting variables and reading the file to tokenization
text = file.read()
words = word_tokenize(text)
ps = PorterStemmer()
# printing the stemming tokenizaiton
for w in words:
    print(ps.stem(w))
