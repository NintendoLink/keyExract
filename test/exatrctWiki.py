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
corpuss=[]

for doc in corpus:
    wordIds=[]
    for wordList in doc:
        wordIds.append(wordList[0])
    corpuss.append(wordIds)


# 生成IDF预训练数据
def IDF(Dict,corpus):
    for doc in corpus:
        for wordList in doc:
            # 得到词
            # print(wordList[0])
            print(inverse(wordList[0],corpuss))
    pass


# 单个词的IDF
def inverse(wordId,corpuss):
    doc_num=len(corpuss)
    include=1
    for doc in corpuss:
        if wordId in doc:
            include+=1
    return doc_num/include
IDF(Dict,corpus)