# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 01:12:40 2016

@author: Vivobook
"""

from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer  # better than porter
from pprint import pprint
from collections import defaultdict
from nltk import word_tokenize
import string
import time
import sys
import logging
import os


logging.basicConfig(filename='D:/workspace/scrap_sg/09022016.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

folder_path = "D:/workspace/scrap_sg/article_test/"
os.chdir(folder_path)

file_lst = os.listdir(".")

stop = stopwords.words('english')
stop

stemmer = SnowballStemmer('english')

# create a corpus
class MyCorpus(corpora.TextCorpus): 
    def get_texts(self): 
        for filename in self.input: # for each relevant file
            with open(filename, "r") as input:
                raw = input.read()
                tokens = word_tokenize(raw)
                words = [w.lower() for w in tokens]  # convert to lower case
                words = [stemmer.stem(w) for w in words if w not in stop] # stem and stop
                words = [w.encode('ascii', 'ignore')
                        for w in words if w not in string.punctuation]  # remove punct.
            yield words

mycorpus = MyCorpus(file_lst)
corpora.MmCorpus.serialize('D:/workspace/scrap_sg/corpus.mm', mycorpus)

# save Dictionary
mycorpus.dictionary.save('D:/workspace/scrap_sg/dictionary.dict')

#sys.stdout.write("\rProgress: " + str((counter/max_len) * 100))
#sys.stdout.flush()
#counter +=1


# creating transformation
#tfidf = models.TfidfModel(mycorpus)
#corpus_tfidf = tfidf[mycorpus]

model = models.ldamulticore.LdaMulticore(mycorpus,
                                         id2word=mycorpus.dictionary,
                                         workers = 2,
                                         iterations=50,
                                         eval_every=10,
                                         passes=20,
                                         num_topics=50)
topic_list = model.print_topics(50)
model.save('D:/workspace/scrap_sg/lda.model')


