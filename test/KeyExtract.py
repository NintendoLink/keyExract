# python 3.6.4
# encoding: utf-8
# 读取原始的语料库文件
import os
import jieba
import jieba.posseg as pseg
import pickle
from gensim import corpora

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
                    documents.append([word for word, flag in sentence if flag in pos_set])
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
def cumputeIDF(Dict,corpus):
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
    with open('IDF_DICT2','wb') as f:
        pickle.dump(IDF_DICT,f)
        f.close()
    return IDF_DICT

# 计算TF值
def computeTF(Dict,document):
    DictItemReversed={tokenid:word for word,tokenid in Dict.items()}
    wordCount={}
    for word in document:
        if word in wordCount.keys():
            wordCount[word]+=1
        else:
            wordCount[word]=1
    for word in wordCount.keys():
        if word not in DictItemReversed.keys():
            wordCount.pop(word)
        else:
            pass
    print(wordCount)
    return wordCount

def computeTFIDF(Dict,IDF_DICT,Document):
    DictItemReversed={tokenid:word for word,tokenid in Dict.item()}
    for word in Document:
        if word in DictItemReversed.keys():
            # 计算TF*IDF
            DictItemReversed.get(word)
            pass
        pass


if __name__ == '__main__':

    # 要保存的内容：
    #     1、Dict 字典
    #     2、documents
    #     3、IDF_DICT

    pos_set = ['ns', 'n']

    # corpus_dir = '../corpora'
    # documents=getDocuments(corpus_dir,pos_flag=True,pos_set=pos_set)

    netEasyCorpusDir='E:/neteasy'
    netEasyCorpusDir = 'E:/corpus/dataset_602151/new4000'
    documents=getNetEasy(netEasyCorpusDir)


    # 构造词典
    # Dict = corpora.Dictionary(documents)
    # with open('DICT2','wb') as f:
    #     Dict.save(f)
    #     f.close()
    Dict = corpora.Dictionary.load(fname='DICT2')
    # print(Dict. token2id){'亿': 9, '亿元': 10, '今年': 11, '其中': 12, '再创':}
    # 构造语料库
    corpus = [Dict.doc2bow(doc) for doc in documents]
    with open('corpus','wb') as f:
        pickle.dump(corpus,f)
        f.close()
    # print(corpus)##[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]]
    cumputeIDF(Dict=Dict,corpus=corpus)
    # document=['高度','财政']
    # computeTF(Dict,document)
