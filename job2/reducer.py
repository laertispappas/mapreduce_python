#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='@'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='@'):
    sum_of_words_in_doc = {}
    tempCounter={}
    
    # input comes from STDIN (standard input) 
    # Input:     document@word=n
    # Output:    word@document#n&N
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_doc - string containing a doc (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_doc, group in groupby(data, itemgetter(0)):
        try:
            for current_doc, word_count in group:
                word = word_count.split('=')[0]
                n = word_count.split('=')[1]
                tempCounter[word + '@' + current_doc] = n
                if current_doc in sum_of_words_in_doc:
                    sum_of_words_in_doc[current_doc] += int(n)
                else:
                    sum_of_words_in_doc[current_doc] = int(n)
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    for wordKey in tempCounter:
        print("%s\t%s/%s") % (wordKey, tempCounter[wordKey], sum_of_words_in_doc[wordKey.split('@')[1]])
if __name__ == "__main__":
    main()

