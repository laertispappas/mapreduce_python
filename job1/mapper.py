#!/usr/bin/env python

import os
import re
import sys
import nltk
from nltk.tokenize import sent_tokenize
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re


file_input = None


def preprocess(sentence):
        #sentence = sentence.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(sentence)
        filtered_words = [w for w in tokens if not w in stopwords.words('english')]
        return filtered_words

def read_input(file):
    for line in file:
        # split the line into words
        yield preprocess(line)

def main(separator='\t'):
    input_file = os.getenv('mapreduce_map_input_file')    
    # input comes from STDIN (standard input) 
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print '%s@%s%s%d' % (word,input_file.split("/")[-1] , separator, 1)

if __name__ == "__main__":
    main()

