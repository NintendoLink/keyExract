# -*- coding: UTF-8 -*-
# python    :3.6
# @Time     :2018/3/16 下午4:05
# @Author   :Link
# @Contact  :wsqihoulin@gmail.com
# @FileName :keyexract2.py
from gensim import corpora,models
import pandas as pd
import jieba
import os
corpus_dir="../corpora"
documents=[]
csv_content=[]
csv_keywords=[]
csv_value=[]

# [(key1,value1),(key2,value2),...,(keyn,valuen)]根据value快速排序
def tupleQucikSort(array):
    less = []
    pivotList = []
    more = []
    if len(array) <= 1:
        return array
    else:
        # 第一个元素作为基准
        pivot=array[0]

        for eleTuple in array:
            if eleTuple[1]<pivot[1]:
                less.append(eleTuple)

            elif eleTuple[1]>pivot[1]:
                more.append(eleTuple)

            else:
                pivotList.append(eleTuple)

        less=tupleQucikSort(less)
        more=tupleQucikSort(more)
        return less+pivotList+more

# 读取原始的语料库文件
for fname in os.listdir(corpus_dir):
    with open(os.path.join(corpus_dir, fname),'r',encoding='utf-8') as f:
        line=f.read()
        csv_content.append(line)
        sentence=jieba.cut(line,cut_all=True)
        # print([word for word in sentence if word != ''])
        documents.append([word for word in sentence if word != ''])


# 构造词典
Dict=corpora.Dictionary(documents)
# 构造语料库
corpus=[Dict.doc2bow(doc) for doc in documents]
# 初始化TF—IDF模型
tf_idf=models.TfidfModel(corpus)
# TF_IDF中的值
for doc in tf_idf[corpus]:
    # print(tupleQucikSort(doc))
    # print(doc)
    print('*******************************')
    for i in range(9):
    # Dict[词的索引编号]
        word=Dict[tupleQucikSort(doc)[i][0]]
        tf_idf_value=tupleQucikSort(doc)[i][1]

        print(word+ "==>>" +str(tf_idf_value)+"  ", end="")

        csv_keywords.append(word)
        csv_value.append(tf_idf_value)

    print()


# 写入csv文件
# c_series=pd.Series(csv_content,name='content')
# k_series=pd.Series(csv_keywords,name='keywords')
# v_series=pd.Series(csv_value,name='value')
#
# content=pd.concat([c_series,k_series,v_series],axis=1)
# content.to_csv("a.csv",encoding='utf-8')
# print(type(content))