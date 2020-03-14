from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os

os.system(r' >output/stemming.txt')

# os.system(r'nul>output/stemming.txt') <-- uncomment it if you work with windows

def stemming(literal):
    """Doing stemming with literal

    :param literal: some data
    """
    ps = PorterStemmer()
    words = word_tokenize(literal)
    f = open('output/stemming.txt', 'w')

    for w in words:
        f.write("Actual: {0}  Stemm: {1}\n".format(w, ps.stem(w)))
    f.close()