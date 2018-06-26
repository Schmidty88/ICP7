from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
file = open('input.txt', 'r', encoding="utf-8")
text = file.read()
words = word_tokenize(text)

print(pos_tag(words))