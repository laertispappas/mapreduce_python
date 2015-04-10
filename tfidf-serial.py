#!/usr/bin/env python
import time
import os
import re
import sys
import nltk
from nltk.tokenize import sent_tokenize
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from math import log10

file_input = None
path = 'test_books'
word_counts = {}
number_of_terms_in_document = {}
number_of_docs_with_term = {}

words_tfidf = {}

def tfidf(word_counts, total_number_of_documents):
    for word_and_doc in word_counts:
        n_terms_appear = int(word_counts[word_and_doc])
        terms_in_doc = int(number_of_terms_in_document[word_and_doc.split('#')[1]])
        words_tfidf[word_and_doc] = [float(n_terms_appear) / float(terms_in_doc)]
        word = word_and_doc.split('#')[0]
        words_tfidf[word_and_doc].append(log10(float(total_number_of_documents) / float(number_of_docs_with_term[word])))
        words_tfidf[word_and_doc].append(words_tfidf[word_and_doc][0] * words_tfidf[word_and_doc][1])
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

def word_count(word, file):
    if word + "#" + file in word_counts:
        word_counts[word + "#" + file] += 1
    else:
        word_counts[word + "#" + file] = 1
        if word in number_of_docs_with_term:
            number_of_docs_with_term[word] += 1
        else:
            number_of_docs_with_term[word] = 1

    if file in number_of_terms_in_document:
        number_of_terms_in_document[file] += 1
    else:
        number_of_terms_in_document[file] = 1

def main(separator='\t'):
    start_time = time.time()
    total_number_of_documents = 0

    for file in os.listdir(path):
        total_number_of_documents += 1
        current = os.path.join(path, file)
        if os.path.isfile(current):
            current_file = open(current)
            data = read_input(current_file)
        for words in data:
            for word in words:
                word_count(word, file)

    tfidf(word_counts, total_number_of_documents)
    with open('out.txt', 'w') as f:
        for word_and_doc in words_tfidf:
            f.write( word_and_doc + "\t" + str(words_tfidf[word_and_doc][0]) + "\t" + str(words_tfidf[word_and_doc][1]) + "\t" + str(words_tfidf[word_and_doc][2]) + "\n")
            f.write(str(time.time() - start_time))
    print "%f seconds" % (time.time() - start_time)

#    print(word_counts)
#    print(number_of_terms_in_document)
#    print(total_number_of_documents)
#    print(number_of_docs_with_term)
#    print(words_tfidf)
if __name__ == "__main__":
    main()

