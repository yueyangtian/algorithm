#-*- coding:utf-8 -*- 
import jieba
import jieba.analyse
import os
import sys
import math


test_file = 'test.txt'
datapath = 'data/allfiles'
stopword_cn_fname = 'stopwords/stopword_cn%d.txt'

#step 1 get stodword set
stop_set_cn = set()
for index in range(1,5):
    with open(stopword_cn_fname % index, 'r') as fd:
            for line in fd:
                    word = line.strip()
                    stop_set_cn.add(word)
#print (stop_set_cn)
jieba.analyse.set_stop_words('stopwords/stopword_cn1.txt')

def get_TF(filename):
        res_dic = dict()
        max_tf = 0
        with open(filename, 'r') as fd:
                for line in fd:
                        #line = list(filter(lambda x,y:x!=' ' and x not in y, jieba.cut(line), stop_set_cn))
                        line = list(filter(lambda x:x!=' ' and x not in stop_set_cn, jieba.cut(line)))
                        for word in line:
                                if word in res_dic.keys():
                                        res_dic[word] = res_dic[word] + 1
                                else:
                                        res_dic[word] = 1
                                if max_tf < res_dic[word]:
                                        max_tf = res_dic[word]
        for term in res_dic.keys():
                #print(term)
                res_dic[term] = float(res_dic[term])/float(max_tf)

        return res_dic


def get_IDF(filedir):
        scan_file_count = 0
        res_dic = dict()
        def merge_set(x,y):
                for tmp in y:
                        x.add(tmp)


        for filename in os.listdir(filedir):
                # for debug
                #if scan_file_count == 2:
                #        break

                filename = filedir + '/' + filename
                with open(filename, 'r') as fd:
                        art_word_set = set()
                        for line in fd:
                                line = list(filter(lambda x:x !=' ' and x not in stop_set_cn, jieba.cut(line)))
                                #lambda x,y:x.add(t) for t in y art_word_set,line
                                merge_set(art_word_set, line)
                        for word in art_word_set:
                                if word in res_dic.keys():
                                        res_dic[word] = res_dic[word] + 1
                                else:
                                        res_dic[word] = 1
                scan_file_count = scan_file_count + 1

        for term in res_dic.keys():
                res_dic[term] = math.log(float(scan_file_count)/float(res_dic[term]+1))
        return res_dic


#print(get_TF(test_file))
#{term:count.....}
idf_dic = get_IDF(datapath)
scan_file_count = 0
for filename in os.listdir(datapath):
        if scan_file_count == 1:
                break
        filename = datapath + '/' + filename
        #{term:tf-score}
        res_dic = get_TF(filename)
        for term in res_dic.keys():
                res_dic[term] = res_dic[term]*idf_dic[term]


        print(res_dic)
        scan_file_count = scan_file_count + 1






