# python 3.6.4
# encoding: utf-8
import pickle
from gensim import corpora
import jieba
import jieba.posseg as pseg
DICT_DIR='IDF_DICT2'
IDF_DIR='DICT2'
CORPUS_DIR='corpus'
IDF={}
DICT=corpora.Dictionary.load('DICT2')

# print(DICT.token2id)

for key in DICT.token2id:
    print(key)
    # print(DICT.token2id[key])
# with open(DICT_DIR,'rb') as f:
#     IDF=pickle.load(f)


# text_dir=''
# pos_set = ['ns', 'n']
# documents=[]
# with open(text_dir,'rb') as f:
#     line=f.readline()
#     sentence = pseg.cut(line)
#     documents.append([word for word, flag in sentence if flag in pos_set])
#
# for key in IDF:
#     # print(key)
#     print(IDF[key])