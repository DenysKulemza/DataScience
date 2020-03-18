from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import re

os.system(r' >output/lemmatizer.txt')

# os.system(r'nul>output/lemmatizer.txt') <-- uncomment it if you work with windows


def lemmatizer(literal):
    """Doing lemmatization with literal

    :param literal: some data
    """
    stop_words = set(stopwords.words('english'))

    word_lemmatizer = WordNetLemmatizer()
    nltk_tokens = word_tokenize(literal)
    words = ''

    f = open('output/lemmatizer.txt', 'w')
    for w in nltk_tokens:
        if re.search(r'[.,?!;:\'()%\s\d"]', w):
            continue
        if w in stop_words:
            continue
        words += '{0} ({1}), '.format(word_lemmatizer.lemmatize(w), w)
    f.write(words)
    f.close()