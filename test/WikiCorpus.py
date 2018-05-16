# python 3.6.4
# encoding: utf-8
import re,os,sys,time
import jieba
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    return cleantext

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        count=0
        for root, dirs, files in os.walk(self.dirname):
            for filename in files:
                file_path = root + '/' + filename
                for line in open(file_path,mode='r',encoding='utf-8'):
                    if line !='\n':
                        sentence = jieba.cut(line)
                        sentList=[word for word in sentence if len(word)>1 and not re.match('^[a-z|A-Z|0-9|.]*$',word)]
                        if len(sentList)>0:
                            yield sentList
                            count+=1
                            # if count %100 ==0:
                            #     print(str(count)+'th'+' sentence')
if __name__ == '__main__':
    defaultParams = {
        'defaultSize': 200,
        'defaultWindow': 10,
        'defaultMinCount': 10,
        'defaultPath': 'D:\chwiki'
    }

    if len(sys.argv)<2:
        print("Please Enter Corpus Path(Wikicorpus/AA/single_Corpus):")
    corpusPath=sys.argv[1]

    begin=time.time()

    mySentences=MySentences(corpusPath)
    model=gensim.models.Word2Vec(sentences=mySentences,
                                 size=defaultParams['defaultSize'],
                                 window=defaultParams['defaultWindow'],
                                 min_count=defaultParams['defaultMinCount'])
    model.save('model.model')
    model.wv.save_word2vec_format("word2vec_org","vocabulary",binary=False)
    end=time.time()
    print("Finished")
    print("Total Processing time: %d seconds " %(end-begin))