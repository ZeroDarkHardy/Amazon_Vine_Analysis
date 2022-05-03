import nltk
from nltk import word_tokenize
text = word_tokenize("I'm trying to enter a new professional field.")
output = nltk.pos_tag(text)
print(output)