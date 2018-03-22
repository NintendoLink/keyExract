# -*- coding: UTF-8 -*-
# python    :3.6
# @Time     :2018/3/19 下午2:37
# @Author   :Link
# @Contact  :wsqihoulin@gmail.com
# @FileName :LSItest.py

# corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
#           [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
#           [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
#           [(0, 1.0), (4, 2.0), (7, 1.0)],
#           [(3, 1.0), (5, 1.0), (6, 1.0)],
#           [(9, 1.0)],
#           [(9, 1.0), (10, 1.0)],
#           [(9, 1.0), (10, 1.0), (11, 1.0)],
#           [(8, 1.0), (10, 1.0), (11, 1.0)]]
#
# corpus.append([(1,1),(2,1)])
#
# tf_idf=models.TfidfModel(corpus)
#
# corpus_tf_idf=tf_idf[corpus]
#
# model=LsiModel(corpus,num_topics=10)
#
# print(model.show_topics())
# for i in model.show_topics():
#     print(i)

from gensim.models import LsiModel
from gensim import corpora,models
import jieba
file_dir="../corpora/test1"
documents=[]
with open(file_dir,"r",encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
        seg_list = jieba.cut(line, cut_all=False)
        sentence=[word for word in seg_list]
        documents.append(sentence)

Dict=corpora.Dictionary(documents)

corpus=[Dict.doc2bow(doc) for doc in documents]

tf_idf=models.TfidfModel(corpus)

lsimodel=LsiModel(corpus=tf_idf[corpus],id2word=Dict,num_topics=4)

# for i in lsimodel[tf_idf[corpus]]:
#     print(i)
for i in lsimodel.show_topics():
    print(i)

# 添加文档
lsimodel.add_documents([[(1,2),(2,1)]])
