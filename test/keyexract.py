# -*- coding: UTF-8 -*-
# python    :3.6
# @Time     :2018/3/16 下午3:37
# @Author   :Link
# @Contact  :wsqihoulin@gmail.com
# @FileName :keyexract.py
from gensim import corpora,models,similarities

texts=[['human','human', 'machine', 'interface', 'lab', 'abc', 'computer', 'applications'],
 ['survey', 'user', 'opinion', 'computer', 'system', 'response', 'time'],
 ['eps', 'user', 'interface', 'management', 'system'],
 ['system', 'human', 'system', 'engineering', 'testing', 'eps'],
 ['relation', 'user', 'perceived', 'response', 'time', 'error', 'measurement'],
 ['generation', 'random', 'binary', 'unordered', 'trees'],
 ['intersection', 'graph', 'paths', 'trees'],
 ['graph', 'minors', 'iv', 'widths', 'trees', 'well', 'quasi', 'ordering'],
 ['graph', 'minors', 'survey']]

dict=corpora.Dictionary(texts)
print(dict)

# 添加文档
new_doc = "Human computer interaction"
new=[new_doc.lower().split()]
# # print(new)
# for i in new:
#     print(i)
# dict.add_documents(new)

# 语料转TF—IDF模型
corpora=[dict.doc2bow(text) for text in texts]
# print(corpora)
tf_idf=models.TfidfModel(corpora)
doc_bow = [(10, 5), (1, 1)]
print(tf_idf[doc_bow])
# 输出TF-IDF
# cor_tf=tf_idf[corpora]
# for i in cor_tf:
#     print(i)
