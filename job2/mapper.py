#!/usr/bin/env python

import os
import re
import sys

file_input = None

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='='):
    #input_file = os.getenv('mapreduce_map_input_file')
    # input comes from STDIN (standard input) 
    data = read_input(sys.stdin)
    for words in data:
        # words = ["word@document, 10"] we need output doc, [word, n]
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        # 
        # tab-delimited; the trivial word count is 1
        
        doc = words[0].split('@')[1]
        word = words[0].split('@')[0]
        n = int(words[1]) 
        print '%s@%s%s%d' % (doc, word,separator, n)

if __name__ == "__main__":
    main()

