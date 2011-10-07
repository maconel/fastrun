#!/usr/bin/python
#coding: utf8

import os

'''
汉字拼音转换库。
pinyin_to_word: 拼音转汉字。
word_to_pinyin: 汉字转拼音。
使用的汉字和拼音均为utf-8编码。参数和返回值也均为utf-8编码。
'''

PINYINFILENAME = r'pinyinlib.txt'
DICT_PINYIN_KEY = {}    #以拼音为key的字典。
DICT_WORD_KEY = {}      #以字为key的字典。


def comb_2list(fun, l1, l2):
    ret = []
    if len(l1) == 0:
        ret = l2
    elif len(l2) == 0:
        ret = l1
    else:
        for i1 in l1:
            for i2 in l2:
                ret.append(fun(i1, i2))
    return ret


def comb(fun, listlist):
    ret = []
    for i in xrange(len(listlist)):
        ret = comb_2list(fun, ret, listlist[i])
    return ret


def _load(filename):
    '''函数作用: 从拼音文件中载入拼音数据。
    参数: filename-指定拼音文件名。
    返回值: 返回2个dict。第一个dict，key是拼音，value是一个list，每项是一个字。第二个dict，key是字，value是一个list，每项是一个拼音。
    '''
    dict_pinyin_key = {}
    dict_word_key = {}

    f = open(filename, 'rt')
    f.readline()    #第一行是列名，不处理。

    for line in f:
        fields = line[: -1].split('\t')
        word = fields[1]    #第2列是字。
        pinyin = fields[4]  #第5列是拼音。

        if dict_pinyin_key.has_key(pinyin):
            dict_pinyin_key[pinyin].append(word)
        else:
            dict_pinyin_key[pinyin] = [word]

        if dict_word_key.has_key(word):
            dict_word_key[word].append(pinyin)
        else:
            dict_word_key[word] = [pinyin]

    f.close()
    return dict_pinyin_key, dict_word_key


def pinyin_to_word(pinyin):
    '''函数作用: 将传入的拼音转为汉字。
    参数: pinyin-传入拼音字符串。
    返回值: 返回一个list，每项是一个字。如果没有对应的字，则返回空list.
    '''
    pinyin = pinyin.lower()
    if DICT_PINYIN_KEY.has_key(pinyin):
        return DICT_PINYIN_KEY[pinyin]
    else:
        return []


def word_to_pinyin(word):
    '''函数作用: 将传入的汉字转为拼音。
    参数: word-传入汉字字符串。
    返回值: 返回一个list，每项是一个拼音。如果没有对应的拼音，则返回空list.
    '''
    if DICT_WORD_KEY.has_key(word):
        return DICT_WORD_KEY[word]
    else:
        return [word]


def word_to_firstchar(word):
    '''函数作用: 将传入的汉字转为拼音首字母。
    参数: word-传入汉字字符串。
    返回值: 返回一个list，每项是一个拼音首字母。如果没有对应的拼音，则返回空list.
    '''
    ret = []
    if DICT_WORD_KEY.has_key(word):
        return [i[0] for i in DICT_WORD_KEY[word]]
    return ret


def wordlist_to_pinyin(wordlist):
    '''函数作用: 将传入的汉字列表转为拼音。
    参数: word-传入汉字列表，或其他可迭代的类型。
    返回值: 返回一个list，每项是一个拼音列表。如果没有对应的拼音，则返回空list.
    '''
    pinyinlistlist = []
    for word in wordlist.decode('utf8'):
        pinyinlistlist.append(word_to_pinyin(word.encode('utf8')))
    return comb(lambda a,b: a+b, pinyinlistlist)


def wordlist_to_pinyin_unique(wordlist):
    '''函数作用: 将传入的汉字列表转为拼音，并去重(多音字可能只是声调不同，拼写是相同的)。
    参数: word-传入汉字列表，或其他可迭代的类型。
    返回值: 返回一个list，每项是一个拼音列表。如果没有对应的拼音，则返回空list.
    '''
    return list_unique(wordlist_to_pinyin(wordlist))


def wordlist_to_firstchar(wordlist):
    '''函数作用: 将传入的汉字列表转为拼音首字母。
    参数: word-传入汉字列表，或其他可迭代的类型。
    返回值: 返回一个list，每项是一个拼音列表，列表中每项是拼音的首字母。如果没有对应的拼音，则返回空list.
    '''
    pinyinlistlist = []
    for word in wordlist.decode('utf8'):
        pinyinlistlist.append(word_to_firstchar(word.encode('utf8')))
    return comb(lambda a,b: a+b, pinyinlistlist)


def fuzzy_pinyin_to_word(pinyin):
    '''函数作用: 将传入的拼音转为汉字。支持模糊查询。即只要pinyin与某汉字拼音的前半部分匹配，即认为匹配了。
    参数: pinyin-传入拼音字符串。
    返回值: 返回一个list，每项是一个字。如果没有对应的字，则返回空list.
    '''
    pinyin = pinyin.lower()
    wordlist = []

    #将所有拼音合成一个大字符串，以'|'间隔，最后一个拼音也以'|'结尾。
    allpinyin = '|'.join(DICT_PINYIN_KEY.keys()) + '|'

    #在allpinyin中找出所有与pinyin匹配的项，并将它所在的整个拼音取出。
    #然后将完整拼音对应的字取出加入结果list.
    pos = 0
    while (pos != -1):
        #找到与'|pinyin'匹配的子字符串。前边加上'|'，是表示pinyin必须从完整拼音的开头比配，不能从中间匹配。
        pos = allpinyin.find('|' + pinyin, pos)
        if pos == -1:
            break
        pos += 1
        #找到后面的'|'.
        pos_end = allpinyin.find('|', pos)
        #取出完整拼音对应的汉字list，加入结果list.
        wordlist.extend(pinyin_to_word(allpinyin[pos : pos_end]))
        pos = pos_end

    return wordlist


#经测试，此方法比fuzzy_pinyin_to_word慢了3倍。
#def fuzzy_pinyin_to_word2(pinyin):
#    '''函数作用: 将传入的拼音转为汉字。支持模糊查询。即只要pinyin与某汉字拼音的前半部分匹配，即认为匹配了。
#    参数: pinyin-传入拼音字符串。
#    返回值: 返回一个list，每项是一个字。如果没有对应的字，则返回空list.
#    '''
#    pinyin = pinyin.lower()
#    wordlist = []
#    for item in DICT_PINYIN_KEY.iteritems():
#        if item[0][: len(pinyin)] == pinyin:
#            wordlist.extend(item[1])
#    return wordlist


def curfilepath():
    return os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), __file__)))

def list_unique(l):
    return {}.fromkeys(l).keys()

DICT_PINYIN_KEY, DICT_WORD_KEY = _load(os.path.join(curfilepath(), PINYINFILENAME))


if __name__ == '__main__':
    '''
    print len(DICT_PINYIN_KEY), len(DICT_WORD_KEY)
    print 'ni:', ', '.join(pinyin_to_word('ni')).decode('utf8')
    print '朝:'.decode('utf8'), ', '.join(word_to_pinyin('朝'))
    print 'ni:', ', '.join(fuzzy_pinyin_to_word('ni')).decode('utf8')
    '''

    '''
    listlist = [['00', '01'], ['10', '11'], [], ['20', '21', '22']]
    print comb(lambda a,b: a+b, listlist)
    '''

    print wordlist_to_pinyin('你好')
    print wordlist_to_firstchar('你好')
