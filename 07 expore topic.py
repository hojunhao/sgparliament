# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 13:37:05 2016

@author: Vivobook
"""

import logging
from gensim import corpora, models, similarities
import os 
from pprint import pprint

folder_path = "D:/workspace/scrap_sg/article_text/"
os.chdir(folder_path)

file_lst = os.listdir(".")


logging.basicConfig(filename='D:/workspace/scrap_sg/09022016.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)
logging.root.level = logging.INFO
                    


dictionary = corpora.Dictionary.load('D:/workspace/scrap_sg/dictionary.dict')
corpus = corpora.MmCorpus('D:/workspace/scrap_sg/corpus.mm')
lda = models.ldamodel.LdaModel.load('D:/workspace/scrap_sg/lda.model')

def print_text(filename):
    with open(filename, "r") as input:
        raw = input.read()
        print raw



lda.print_topics(50)

    
index = similarities.MatrixSimilarity(lda[corpus])
index.save("D:/workspace/scrap_sg/simIndex.index")

doc_lda = lda[corpus]

# inspect one doc
def inspect_corpus(index, doc_lda, file_lst):
    pprint(doc_lda[index])
    print file_lst[index]
    topics = [topic for topic, weight in doc_lda[index]]
    for i in range(0, lda.num_topics):
        if i in topics:
            print "TOPIC " + str(i) + ":" + str(lda.print_topic(i))
            print "\n"
    print_text(file_lst[index])



inspect_corpus(470, doc_lda, file_lst)
#
#i = 1761
#pprint(doc_lda[i])
#print file_lst[i]
#topics = [topic for topic, weight in doc_lda[i]]
#for i in range(0, lda.num_topics-1):
#    if i in topics:
#        print "TOPIC " + str(i) + ":" + str(lda.print_topic(i))
#        print "\n"
#print_text(file_lst[i])

counter = 0
for c in corpus:
    length = len(c)
    if length >30  and length <50:
        print counter
    counter += 1








    