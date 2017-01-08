# coding=utf-8
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

# 返回词组和词    增加几率
def bigrams_word(words, score_fn = BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return word_feats(bigrams + words)

def store_classifier(classifier ,filepath):
    # use pickle to store classifier
    pickle.dump(classifier, open(filepath,'w'))


if __name__ == '__main__':
    negids = cut_at_path('comment_neg.txt')
    posids = cut_at_path('comment_pos.txt')

    negfeats = [(bigrams_word(f), 'neg') for f in negids]
    posfeats = [(bigrams_word(f), 'pos') for f in posids]

    ##print negfeats[:5]

    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4

    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
    print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
    
    classifier = NaiveBayesClassifier.train(trainfeats)
    store_classifier(classifier,'sentiment_classifier.pkl')

    
    print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
    classifier.show_most_informative_features()

    # 测试一个数据
    print classifier.classify(word_feats(jieba.lcut("今天股票好")))

