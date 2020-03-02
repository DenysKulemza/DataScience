from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import time
import logging

logging.basicConfig(filename='RunTime.log', level=logging.INFO, format='%(message)s')


def stemming(literal):
    ps = PorterStemmer()
    words = word_tokenize(literal)
    f = open('stemming.txt', 'w')

    for w in words:
        f.write("Actual: {0}  Stemm: {1}\n".format(w, ps.stem(w)))
    f.close()


def lemmatizer(literal):
    word_lemmatizer = WordNetLemmatizer()
    nltk_tokens = word_tokenize(literal)
    f = open('lemmatizer.txt', 'w')
    for w in nltk_tokens:
        f.write("Actual: {0}  Lemma: {1}\n".format (w, word_lemmatizer.lemmatize(w)))
    f.close()


if __name__ == '__main__':
    f = open('text.txt', 'r')
    text = ''
    for s in f:
        text += s
    f.close()

    s = time.time()
    stemming(text)
    logging.info(f'Run time Stemming {str(time.time() - s)}')

    s = time.time()
    lemmatizer(text)
    logging.info(f'Run time Lemmatizer {str(time.time() - s)}')

