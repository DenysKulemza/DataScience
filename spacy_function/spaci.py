import spacy
import re

import os

os.system(r' >output/spacy.txt')

# os.system(r'nul>output/spacy.txt') <-- uncomment it if you work with windows

nlp = spacy.load('en_core_web_sm')


def spacy_lemma(literal):
    """Doing lemmatization with literal by spacy library

        :param literal: some data
        """
    our_string = nlp(literal)
    f = open('output/spacy.txt', 'w')
    for w in our_string:
        f.write("Actual: {0}  Lemma: {1}\n".format(w, w.lemma_))
    f.close()