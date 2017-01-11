# -*- coding:utf-8 -*-
import DBTools as dbtools
import pickle                       # 把对象存到文件中去
import jieba
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder

# 按文件路径切词,返回一个列表的列表(特征提取器)
def cut_at_path(path):
    with open(path) as f:
        r = f.read()
    sentences = r.split('\n')
    words = []
    for each in sentences:
        words.append(jieba.lcut(each))
    return words

# bag of words model (词袋模型)
def word_feats(words):
    return dict([(word, True) for word in words])

# return value of postive
def pos_value(stock_code):
    claf = pickle.load(open('comment_scraper/sentiment_analy/sentiment_classifier.pkl'))
    # claf = pickle.load(open('sentiment_classifier.pkl'))
    lists = dbtools.select_by_stock_code(stock_code)
    count = 0.0
    count_pos = 0.0
    for each in lists:
        result = claf.classify(word_feats(jieba.lcut(each[0])))
        if result=='pos':
            count_pos+=1
        count+=1
##    print "positive:  %.2f" % (count_pos/count)
    return "%.2f" % (count_pos/count)

def save_to_db(stock_code):
    ss_list = ["","",""]
    tupler = dbtools.select_two(stock_code)
    ss_list[0] = tupler[0]
    ss_list[1] = tupler[1]
    ss_list[2] = pos_value(stock_code)
    dbtools.insert_sentiment(ss_list)
    return ss_list[2]
    


if __name__ == '__main__':
    print save_to_db(600000)



