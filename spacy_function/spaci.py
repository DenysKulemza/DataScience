from spacy.lang.en import English
import spacy
import os
import re

os.system(r' >output/spacy.txt')

# os.system(r'nul>output/spacy.txt') <-- uncomment it if you work with windows

nlp = English()


def spacy_lemma(literal):
    """Doing lemmatization with literal by spacy library

        :param literal: some data
        """
    our_string = nlp(literal)
    words = ''

    all_words = 0
    transform_words = 0

    token_list = []
    for token in our_string:
        token_list.append(token.text)

    f = open('output/spacy.txt', 'w')

    filtered = ''

    for w in token_list:
        if re.search(r'[.,?!;:\-\'()%\s\d\"]', str(w)):
            continue
        lexeme = nlp.vocab[w]
        if lexeme.is_stop:
            continue
        filtered += ' ' + str(w)

    nlp_1 = spacy.load('en_core_web_sm')
    literal = nlp_1(filtered)

    for w in literal:
        words = '{0} ({1}), '.format(w.lemma_, w)
        all_words += 1

        f.write(words)

        if str(w) != str(w.lemma_):
            transform_words += 1

    f.write(f'\n Amount of words: {all_words}')
    f.write(f'\n Amount of transform words: {transform_words}')
    f.write(f'\n Correct transform words: {transform_words} - 100%')

    f.close()
