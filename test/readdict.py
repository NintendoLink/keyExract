# python 3.6.4
# encoding: utf-8
import pickle
from gensim import corpora
from test import keyextract
DICT_DIR='IDF_DICT2'
CORPUS_DIR='corpus'
IDF={}
DICT=corpora.Dictionary.load('DICT2')

# print(DICT.token2id)

# for key in DICT.token2id:
#     print(key)
#     print(DICT.token2id[key])

with open(DICT_DIR,'rb') as f:
    IDF=pickle.load(f)


for key in IDF:
    # print(key)
    print(IDF[key])

