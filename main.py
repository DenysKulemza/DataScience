from nltk_function.lemmatizer import *
from nltk_function.stemming import *
from spacy_function.spaci import *
import time
import logging

logging.basicConfig(filename='output/RunTime.log', level=logging.INFO, format='%(message)s')

file_path = 'data_sets/sport.txt'

if __name__ == '__main__':
    f = open(file_path, 'r')
    text = ''
    for s in f:
        text += s
    f.close()

    logging.info(f'Time with following data set: {file_path}')
    s = time.time()
    stemming(text)
    logging.info(f'Run time Stemming {str(time.time() - s)}')

    s = time.time()
    lemmatizer(text)
    logging.info(f'Run time Lemmatizer {str(time.time() - s)}')

    s = time.time()
    spacy_lemma(text)
    logging.info(f'Run time Spacy {str(time.time() - s)}')
    logging.info('===========================================')