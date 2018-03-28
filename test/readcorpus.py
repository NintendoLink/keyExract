# python 3.6.4
# encoding: utf-8
import os
import jieba
import jieba.posseg as pseg
from gensim import corpora


corpus_dir='../corpora'
documents=[]
pos_set=['ns','n']
for fname in os.listdir(corpus_dir):
    with open(os.path.join(corpus_dir, fname),'r',encoding='utf-8') as f:
        line=f.read()
        words=pseg.cut(line)
        documents.append([word for word,flag in words if flag in pos_set])

for i in documents:
    print(i)

Dict=corpora.Dictionary(documents)
for item,a in Dict.items():
    print(item,a)
corpus=[Dict.doc2bow(doc) for doc in documents]
