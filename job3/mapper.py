#!/usr/bin/env python

import os
import re
import sys

file_input = None

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    """ 
     Map input:   word@document \t n/N
         output:  word, [document=n/N, ...] or word@document#n/N
    """
    # data = [word@document \t n/N]
    data = read_input(sys.stdin)
    for words in data:
        # words = ["word@document",  "n/N"]
        doc = words[0].split('@')[1]
        word = words[0].split('@')[0]
        N = int(words[1].split('/')[1])
        n = int(words[1].split('/')[0])
        print '%s@%s%s%d/%d' % (word, doc,separator, n, N)

if __name__ == "__main__":
    main()

