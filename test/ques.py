# -*- coding: UTF-8 -*-
# python    :3.6
# @Time     :2018/3/16 下午4:24
# @Author   :Link
# @Contact  :wsqihoulin@gmail.com
# @FileName :ques.py
import jieba

str="小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
print([word for word in jieba.cut(str,cut_all=True) if word != ""])
# for i in jieba.cut(str,cut_all=True):
#     print(i)
