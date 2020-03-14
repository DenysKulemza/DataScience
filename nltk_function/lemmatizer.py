from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import os

os.system(r' >output/lemmatizer.txt')

# os.system(r'nul>output/lemmatizer.txt') <-- uncomment it if you work with windows


def lemmatizer(literal):
    """Doing lemmatization with literal

    :param literal: some data
    """
    word_lemmatizer = WordNetLemmatizer()
    nltk_tokens = word_tokenize(literal)

    f = open('output/lemmatizer.txt', 'w')
    for w in nltk_tokens:
        f.write("Actual: {0}  Lemma: {1}\n".format (w, word_lemmatizer.lemmatize(w)))
    f.close()