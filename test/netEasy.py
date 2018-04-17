# python 3.6.4
# encoding: utf-8
import os
import jieba
import jieba.posseg as pseg
# 读取新闻数据集，二级目录文档
def getNetEasy(corpus_dir,pos_flag=False,pos_set=[],random_flag=False,rate=0.1):
    documents=[]
    for listDir in os.listdir(corpus_dir):
        for fname in os.listdir(corpus_dir+'/'+listDir):
            with open(os.path.join(corpus_dir+'/'+listDir,fname),'r',encoding='utf-8') as f:
                line = f.read()
                if pos_flag:
                    sentence = pseg.cut(line)
                    documents.append([word for word, flag in sentence if flag in pos_set])
                else:
                    sentence = jieba.cut(line)
                    documents.append([word for word in sentence if word != ''])
    # print(len(documents))
    # for doc in documents:
    #     print(doc)
if __name__ == '__main__':
    netEasyCorpusDir='E:/neteasy'
    getNetEasy(netEasyCorpusDir)