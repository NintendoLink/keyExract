# python 3.6.4
# encoding: utf-8
# 读取原始的语料库文件
import os
import jieba
import jieba.posseg as pseg
from gensim import corpora
corpus_dir='../corpora'
pos_set=['ns','n']

def getDocuments(corpus_dir,pos_flag=False,pos_set=[]):
    documents = []
    for fname in os.listdir(corpus_dir):
        with open(os.path.join(corpus_dir, fname), 'r', encoding='utf-8') as f:
            line = f.read()
            if pos_flag:
                sentence = pseg.cut(line)
                # print([word for word in sentence if word != ''])
                documents.append([word for word, flag in sentence if flag in pos_set])
                # documents.append([word for word in sentence if word != ''])
            else:
                sentence = jieba.cut(line)
                # print([word for word in sentence if word != ''])
                documents.append([word for word in sentence if word != ''])
    return documents

def cumputeIDF(documents):
    # 构造词典
    Dict = corpora.Dictionary(documents)
    IDF_DICT={}
    # print(Dict. token2id){'亿': 9, '亿元': 10, '今年': 11, '其中': 12, '再创':}
    # 构造语料库
    corpus = [Dict.doc2bow(doc) for doc in documents]
    # print(corpus)##[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]]
    corpuss = []

    for doc in corpus:
        wordIds = []
        for wordList in doc:
            wordIds.append(wordList[0])
        corpuss.append(wordIds)

    for doc in corpus:
        for wordList in doc:
            include_num = 1
            # 计算单个词的idf，相同词的IDF值理论上应该相同
            for doc in corpuss:
                if wordList[0] in doc:
                    include_num += 1
            # print(len(corpuss)/include_num)
            # print(str(wordList[0])+'===>'+str(len(corpuss)/include_num))
            if wordList[0] not in IDF_DICT.keys():
                IDF_DICT[wordList[0]] = len(corpuss) / include_num
            else:
                pass
    for item in IDF_DICT.items():
        print(str(Dict[item[0]])+'======>'+str(item[1]))

    return Dict,IDF_DICT

def computeTFIDF(Dict,IDF_DICT,Document):


    DictItemReversed={tokenid:word for word,tokenid in Dict.item()}
    for word in Document:
        if word in DictItemReversed.keys():
            # 计算TF*IDF
            DictItemReversed.get(word)
            pass
        pass

# 计算TF值
def computeTF(Dict,document):
    DictItemReversed={tokenid:word for word,tokenid in Dict.item()}
    wordCount={}
    for word in document:
        if word in wordCount.keys():
            wordCount[word]+=1
        else:
            wordCount[word]=0
    for word in wordCount.keys():
        if word not in DictItemReversed.keys():
            wordCount.pop(word)
        else:
            pass
    print(wordCount)
    return wordCount

if __name__ == '__main__':
    docs = getDocuments(corpus_dir, pos_flag=True, pos_set=pos_set)
    cumputeIDF(docs)
