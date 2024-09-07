'''
jieba 库
    1.jieba 简介：
    jieba 是中文分词函数库，能够将一段中文文本分割成中文词语的序列

    2.使用 jieba 进行分词：
        函数名                                 描述
        jieba.lcut(s)                         精确模式，返回一个列表类型；参数 s 即目标要分的词
        jieba.lcut(s, cut_all = True)         全模式，返回一个列表类型
        jieba.lcut_for_search(s)              搜索引擎模式，返回一个列表类型
        jieba.add_word(w)                     向分词词典中增加新词
'''
import jieba

# 1.jieba.lcut(s)
list1 = jieba.lcut('国家计算机二级考试Python学科')
print(list1) # return ['国家', '计算机', '二级', '考试', 'Python', '学科']

# 2.jieba.lcut(s, cut_all = True)
list2 = jieba.lcut('国家计算机二级考试Python学科', cut_all = True)
print(list2) # return ['国家', '家计', '计算', '计算机', '算机', '二级', '考试', 'Python', '学科'] -- 即返回更多潜在的中文词语

# 3.jieba.lcut_for_search(s)
list3 = jieba.lcut_for_search('国家计算机二级考试Python学科')
print(list3) # return ['国家', '计算', '算机', '计算机', '二级', '考试', 'Python', '学科'] -- 即首先进行精确模式，再附加全模式

# 4.jieba_add_word(w)
jieba.add_word('Python学科')
list4 = jieba.lcut('国家计算机二级考试Python学科')
print(list4) # return ['国家', '计算机', '二级', '考试', 'Python学科'] -- 因为向分词库中添加了 'Python学科' 这一新的分词，导致结果也和默认不同

