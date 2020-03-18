from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import re

os.system(r' >output/stemming.txt')

# os.system(r'nul>output/stemming.txt') <-- uncomment it if you work with windows

def stemming(literal):
    """Doing stemming with literal

    :param literal: some data
    """

    stop_words = set(stopwords.words('english'))
    word = ''

    ps = PorterStemmer()
    words = word_tokenize(literal)
    f = open('output/stemming.txt', 'w')

    for w in words:
        if re.search(r'[.,?!;:\'()%\s\d"]', w):
            continue
        if w in stop_words:
            continue
        word += "{0} ({1}), ".format(ps.stem(w), w)
    f.write(word)
    f.close()