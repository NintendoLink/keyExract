# python 3.6.4
# encoding: utf-8

import os
import jieba.analyse
corpora_dir='../corpora/test1'
with open(corpora_dir,'r',encoding='utf-8') as f:
    line=f.read()
# print(line)


# 设置停用词列表
jieba.analyse.set_stop_words('../corpora/stopwords')
# 预训练的IDF值
# *******************
# 文档格式如下
# 劳动防护 13.900677652
# 勞動防護 13.900677652
# 生化学 13.900677652
# 生化學 13.900677652
# 奥萨贝尔 13.900677652
# 奧薩貝爾 13.900677652
# 考察队员 13.900677652
# 考察隊員 13.900677652
# *******************

# jieba.analyse.set_idf_path('../corpora')

# sentence 为待提取的文本
# topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
# withWeight 为是否一并返回关键词权重值，默认值为 False
# allowPOS 仅包括指定词性的词，默认值为空，即不筛选
print(jieba.analyse.extract_tags(line,10,True))#[('城市', 0.43128446190484426), ('销售价格', 0.2813089578328028), ('三线', 0.2265370228531488), ('商品住宅', 0.21717448453961938)]