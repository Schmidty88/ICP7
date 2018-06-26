from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

file = open('input.txt', 'r', encoding="utf-8")
text = file.read()
words = word_tokenize(text)

print(ne_chunk(pos_tag(words)))