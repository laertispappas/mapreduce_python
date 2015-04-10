#!/usr/bin/env python

import os
import re
import sys
from nltk.tokenize import sent_tokenize
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re


file_input = None

def read_input(file):
    for line in file:
        # split the line into words
        yield preprocess(line)

def preprocess(sentence):
	#sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	return filtered_words

def main(separator='\t'):
    # input comes from STDIN (standard input) 
    data = read_input(sys.stdin)

    for words in data:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        print(words)
if __name__ == "__main__":
    main()

