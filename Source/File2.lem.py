# needed library
import nltk
nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# file write
file = open('input.txt', 'r', encoding="utf-8")
text = file.read()
lem = WordNetLemmatizer()
words = word_tokenize(text)
# this for loop is going though and making sure each word is being changed properly then outputed
for word in words:
    print(lem.lemmatize(word, pos='v'))
