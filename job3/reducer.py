#!/usr/bin/env python

#mapreduce.input.num.files


from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='@'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='@'):
    num_of_docs_in_corpus_where_key_appears = {}
    word_doc_freq = {}

    # Input:     word@document \t n/N=1
    # Output:    word@document \t n/N=M
    data = read_mapper_output(sys.stdin, separator=separator)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            for current_word2, doc_n_N in group:
                # current word = word, doc_n_N = doc \t n/N
                doc_and_frequencies = doc_n_N.split('\t')
                if current_word2 in num_of_docs_in_corpus_where_key_appears:
                    num_of_docs_in_corpus_where_key_appears[current_word2] += 1
                else:
                    num_of_docs_in_corpus_where_key_appears[current_word2] = 1
                word_doc_freq[current_word2] = [doc_and_frequencies[0], doc_and_frequencies[1]]
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    for word in num_of_docs_in_corpus_where_key_appears:
        print "%s@%s\t%s=%d" % (word, word_doc_freq[current_word][0], word_doc_freq[word][1], num_of_docs_in_corpus_where_key_appears[word])

        
    #for wordKey in tempCounter:
        #print("%s#%s&%s") % (wordKey, tempCounter[wordKey], sum_of_words_in_doc[wordKey.split('@')[1]])
if __name__ == "__main__":
    main()

