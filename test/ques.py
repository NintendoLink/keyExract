# python 3.6.4
# encoding: utf-8
import os
# corpus_dir='../corpora'
# copora=[]
# for fname in os.listdir(corpus_dir):
#     with open(os.path.join(corpus_dir,fname),'r',encoding='utf-8') as f:
#         copora.append(f.read())
#         # print(f.read())
#
# print(len(copora))
# for i in copora:
#     print(i)


import sys
# python 3.6.4
# encoding: utf-8
# 读取原始的语料库文件
import os
import jieba
from gensim import corpora
corpus_dir='../corpora'
documents=[]
for fname in os.listdir(corpus_dir):
    with open(os.path.join(corpus_dir, fname),'r',encoding='utf-8') as f:
        line=f.read()
        sentence=jieba.cut(line,cut_all=True)
        # print([word for word in sentence if word != ''])
        documents.append([word for word in sentence if word != ''])


# 构造词典
Dict=corpora.Dictionary(documents)
# print(Dict. token2id){'亿': 9, '亿元': 10, '今年': 11, '其中': 12, '再创':}
# 构造语料库
corpus=[Dict.doc2bow(doc) for doc in documents]
# print(corpus)##[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]]
# corpuss=[[]]
# for doc in corpus:
#     wordId=[]
#     for wordList in doc:
#         wordId.append(wordList[0])
#     corpuss.append(wordId)
#
# for i in corpuss:
#     print(i)
# for i in Dict.keys():
#     print(i)

# for key,val in Dict.token2id:
#     print(str(key)+"====>"+str(val))
# print(type(Dict.token2id))
# print(Dict.token2id)
# print(Dict.token2id['上映'])
# dict2={k:z for z,k in Dict.token2id.items()}
# print(dict2)

for item in Dict.items():
    print(item)