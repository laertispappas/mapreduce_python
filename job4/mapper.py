#!/usr/bin/env python

import os
import re
import sys
from math import log

file_input = None

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main():
    """ 
     D = Number of documents is known
     calculate TD-IDF based on n;N;m and D. D is known ahead of time.
     TFIDF = n/N * log(D/m) 
     
     input:   word@document \t n/N=m
     output:  word@document, m/D, n/N, TFIDF
    """
    D = os.getenv('DOCS')
    if (not D):
        print "Error exporting number if documents"
        sys.exit()
    data = read_input(sys.stdin)
    for words in data:
        # words = ["word@document",  "n/N=m"]
        word = words[0].split('@')[0]
        doc = words[0].split('@')[1]
        n = words[1].split('/')[0]
        N = words[1].split('/')[1].split('=')[0]
        m = words[1].split('=')[1]
        tf = float(n)/float(N)
        idf = log((float(D)/float(m)), 10)
        print "%s@%s,\t %s/%s, \t %s, \t %s" % (word, doc, m, D, float(n)/float(N), tf*idf)
if __name__ == "__main__":
    main()

