# python 3.6.4
# encoding: utf-8
from gensim import corpora
Dict=corpora.Dictionary.load(fname='../Dict2')
print(Dict)