# -*- coding: UTF-8 -*-
# python    :3.6
# @Time     :2018/3/20 下午5:02
# @Author   :Link
# @Contact  :wsqihoulin@gmail.com
# @FileName :jiebatest.py
import jieba
# import jieba.analyse.analyzer

with open("../corpora/test1","r",encoding='utf-8') as f:
    line=f.read()
    seg_list=jieba.cut(line, cut_all=True)
# result=jieba.analyse.extract_tags(line,topK=10)
# print(result)
