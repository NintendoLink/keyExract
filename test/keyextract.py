# python 3.6.4
# encoding: utf-8
# 读取原始的语料库文件
import os
import jieba
import jieba.analyse
import jieba.posseg as pseg
import pickle
from gensim import corpora

def getDocument(corpus_dir,pos_flag=False,pos_set=[]):
    pass
# 单级目录的文档读取
def getDocuments(corpus_dir,pos_flag=False,pos_set=[]):
    documents = []
    for fname in os.listdir(corpus_dir):
        with open(os.path.join(corpus_dir, fname), 'r', encoding='utf-8') as f:
            line = f.read()
            if pos_flag:
                sentence = pseg.cut(line)
                documents.append([word for word, flag in sentence if flag in pos_set])
            else:
                sentence = jieba.cut(line)
                documents.append([word for word in sentence if word != ''])
    return documents

# 读取新闻数据集，二级目录文档
def getNetEasy(corpus_dir,pos_flag=False,pos_set=[],random_flag=False,rate=0.1):
    jieba.analyse.set_stop_words('../stopwords/stopwords')
    file_count=1
    documents=[]
    for listDir in os.listdir(corpus_dir):
        for fname in os.listdir(corpus_dir+'/'+listDir):
            if(file_count%100 ==0):
                print("正在处理第"+str(file_count)+"篇文档....")
            with open(os.path.join(corpus_dir+'/'+listDir,fname),'r',encoding='utf-8') as f:
                line = f.read()
                if pos_flag:
                    sentence = pseg.cut(line)
                    # 判断词性集合，剔除单个词
                    documents.append([word for word, flag in sentence if flag in pos_set and not len(word)<2])
                else:
                    sentence = jieba.cut(line)
                    documents.append([word for word in sentence if word != ''])
            file_count+=1
    print("documents finished！")
    print("documentLength: "+str(len(documents)))
    return documents
    # print(len(documents))
    # for doc in documents:
    #     print(doc)
def cumputeIDF(corpus):
    corpus_count=1
    IDF_DICT={}
    corpuss = []
    # corpuss [[1,2,3,4,5,6],[2,6,7,10]....[]]
    for doc in corpus:
        wordIds = []
        for wordList in doc:
            wordIds.append(wordList[0])
        corpuss.append(wordIds)
    corpuss_len=len(corpuss)

    for doc in corpus:
        if(corpus_count%100==0):
            print('正在计算第'+str(corpus_count)+'篇文文章的IDF...')
        for wordList in doc:
            include_num = 1
            if wordList[0] not in IDF_DICT.keys():
                # 计算单个词的idf，相同词的IDF值理论上应该相同
                for doc in corpuss:
                    if wordList[0] in doc:
                        include_num += 1
                IDF_DICT[wordList[0]] = corpuss_len / include_num
        corpus_count+=1

    # for cor in corpuss:
    #     if(corpus_count%100==100):
    #         print('正在计算第' + str(corpus_count) + '篇文文章的IDF...')
    #     for word2id in cor:
    #         include_num=1
    #         if word2id  not in IDF_DICT.keys():
    #             for cor2 in corpuss:
    #                 if word2id in cor2:
    #                     include_num+=1
    #             IDF_DICT[word2id]=corpuss_len/include_num

    return IDF_DICT

# 计算TF值
def computeTF(document):
    wordCount={}
    for word in document:
        if word[0] in wordCount.keys():
            wordCount[word[0]]+=1
        else:
            wordCount[word[0]]=1
    return wordCount

def computeTFIDF(IDF_DICT,TF_wordCount):
    # 1.把document进行token2id
    # 2.遍历TF_wordcount
    #     2.1 查找IDF_DICT
    #     2.2 存储TF*IDF
    TFMultiIDF={}

    for token2id in  TF_wordCount.keys():
        TFMultiIDF[token2id]=TF_wordCount[token2id]*IDF_DICT[token2id]
    return TFMultiIDF

def save(dictDir,idfDir,corpusDir):
    # 要保存的内容：
    #     1、Dict 字典
    #     2、documents
    #     3、IDF_DICT

    pos_set = ['ns', 'n', 'v', 'a']

    # corpus_dir = '../corpora'
    # documents=getDocuments(corpus_dir,pos_flag=True,pos_set=pos_set)

    # netEasyCorpusDir='E:/neteasy'
    netEasyCorpusDir = 'E:/corpus/dataset_602151/new4000'
    documents = getNetEasy(netEasyCorpusDir, pos_flag=True, pos_set=pos_set)
    # documents=getNetEasy(netEasyCorpusDir)

    # 构造词典
    Dict = corpora.Dictionary(documents)
    with open(dictDir, 'wb') as f:
        Dict.save(f)
        f.close()
    # Dict = corpora.Dictionary.load(fname='DICT2')
    # print(Dict. token2id){'亿': 9, '亿元': 10, '今年': 11, '其中': 12, '再创':}
    # 构造语料库
    corpus = [Dict.doc2bow(doc) for doc in documents]
    # 保存语料库
    with open('corpus', 'wb') as f:
        pickle.dump(corpus, f)
        f.close()
    # print(corpus)##[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]]
    idfDict=cumputeIDF(corpus=corpus)

    # 保存IDF词典
    with open('IDF_DICT2','wb') as f:
        pickle.dump(idfDict,f)
        f.close()

def load(dictDir,idfDir,corpusDir):
    Dict = corpora.Dictionary.load(dictDir)
    IDF = {}
    with open(idfDir, 'rb') as f:
        IDF = pickle.load(f)

    documentText = ['高度', '财政']
    documents = Dict.doc2bow(documentText)
    wordCount = computeTF(documents)
    return computeTFIDF(IDF, wordCount)

if __name__ == '__main__':
    dictDir="DICT2"
    idfDir="IDF_DICT2"
    corpusDir="corpus"

    tf_idf=load(dictDir,idfDir,corpusDir)

    for word2id in tf_idf:
        print(tf_idf[word2id])