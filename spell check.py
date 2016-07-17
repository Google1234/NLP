#-*- coding: UTF-8 -*-
from depend import *
import time
def make_trie(words):
    print "---->Begin sort words"
    sort=quick_sort(words)
    #sort.show()
    words=sort.sort(1,len(words)-1)
    #sort.show()
    print "---->Finish sort words:",words
    print "---->Begin make trie"
    #initiate
    buff=[]
    pointer=0
    last_word=['' for i in range(15)]
    last_word_letter_index_information=[0 for i in range(15)]
    last_length=0

    buff.append(['',0,0])
    pointer=0
    last_word=''
    last_word_letter_index_information[0]=0
    last_length=1
    #run
    for word in words:
        length=len(word)
        t=min(length,last_length)
        while last_word[:t]!=word[:t]:
            t-=1
        #first
        brother=last_word_letter_index_information[t]
        buff.append([word[t],0,0])
        pointer+=1
        buff[brother][2]=pointer #brother
        last_word_letter_index_information[t]=pointer
        parent=pointer
        t+=1
        while t<length:
            buff.append([word[t],0,0])
            pointer+=1
            buff[parent][1]=pointer #child
            last_word_letter_index_information[t]=pointer
            parent=pointer
            t+=1
        #last : ''
        buff.append(['',0,0])
        pointer+=1
        buff[parent][1]=pointer #child
        last_word_letter_index_information[t]=pointer

        last_word=word+''
        last_length=len(word)
    return buff
def make_trie_from_txtFile(filename):
    print "---->Begin read words from File"
    start=time.time()
    f=open(filename)
    words=[]
    word=f.readline()
    while word:
        words.append(word[:-1])
        word=f.readline()
    f.close()
    print "---->Finish read words from File"

    print "---->Begin sort words"
    sort=quick_sort(words)
    #sort.show()
    words=sort.sort(1,len(words)-1)
    #sort.show()
    print "---->Finish sort words:"
    print "---->Begin make trie"
    #initiate
    buff=[]
    pointer=0
    last_word=['' for i in range(50)]
    last_word_letter_index_information=[0 for i in range(50)]
    last_length=0

    buff.append(['',0,0])
    pointer=0
    last_word=''
    last_word_letter_index_information[0]=0
    last_length=1
    #run
    for word in words:
        if word!=last_word and word!='':#去词典重复的单词 读的词项中有''空字符，与结束符冲突
            length=len(word)
            t=min(length,last_length)
            while last_word[:t]!=word[:t]:
                t-=1
            #first
            brother=last_word_letter_index_information[t]
            buff.append([word[t],0,0])
            pointer+=1
            buff[brother][2]=pointer #brother
            last_word_letter_index_information[t]=pointer
            parent=pointer
            t+=1
            while t<length:
                buff.append([word[t],0,0])
                pointer+=1
                buff[parent][1]=pointer #child
                last_word_letter_index_information[t]=pointer
                parent=pointer
                t+=1
            #last : ''
            buff.append(['',0,0])
            pointer+=1
            buff[parent][1]=pointer #child
            last_word_letter_index_information[t]=pointer
            last_word=word+''
            last_length=len(word)
    end=time.time()
    print "time cost:",end-start
    return buff
def look(word,trie):
    pointer=0
    exist=True
    for c in word:
        while c!=trie[pointer][0]:
            pointer=trie[pointer][2]
            if pointer==0:
                exist=False
                break
        if exist:
           pointer=trie[pointer][1]
        else:
            break
    if ''!=trie[pointer][0]:
        exist=False
    print word, "exist?---->",exist
    return exist
def calulate_distance(word1,word2):
    word1='#'+word1
    word2='#'+word2
    distance=[[0 for i in range(len(word2))] for j in range(len(word1))]
    for i in range(len(word1)):
        distance[i][0]=i
    for j in range(len(word2)):
        distance[0][j]=j
    for i in range(len(word1)-1):
        for j in range(len(word2)-1):
            if word1[i+1]==word2[j+1]:
                distance[i+1][j+1]=distance[i][j]
            else:
                if word1[i]==word2[j+1] and word1[i+1]==word2[j]:
                    distance[i + 1][j + 1] = 1+min(distance[i-1][j-1],distance[i][j+1],distance[i+1][j])
                else:
                    distance[i + 1][j + 1] = 1 + min(distance[i][j], distance[i][j + 1], distance[i + 1][j])
    return distance[len(word1)-1][len(word2)-1]
class spell_check:
    def __init__(self,trie):
        self.trie=trie
    def search(self,front_part,child):
        pointer=child
        while 1:
            c=self.trie[pointer][0]
            if c=='':
                correct_word = front_part
                d = calulate_distance(self.word, correct_word)
                if d <= self.tol:
                    self.similar.append([d,correct_word])
            else:
                trie_word=front_part+c
                m=len(trie_word)
                l=max(1,m-self.tol)
                u=min(self.word_length,m+self.tol)
                min_distance=100
                for i in range(l, u+1):
                    min_distance=min(min_distance,calulate_distance(self.word[:i], trie_word))
                if min_distance <= self.tol and self.trie[pointer][0]!='':
                    self.search(trie_word,self.trie[pointer][1])#child
            pointer=self.trie[pointer][2]#brother
            if pointer==0:
                break
    def spell_check(self,word,tol=3,topK=5):
        '''
        :param trie:
        :param word:
        :param tol: 允许拼写错误的次数
        :return:
        '''
        self.word = word
        self.tol = tol
        self.word_length = len(word)
        self.similar=[]
        self.search('',0)
        print "Input word:",word
        print "Top ",topK," Correct word:"
        if self.similar!=[]:
            sort=quick_sort_Multidimensional_Data(self.similar)
            sort.sort(0,len(self.similar)-1)
            for i in range(topK):
                if i<len(self.similar):
                    print sort.a[i]
                else:
                    break

#words=['aq','ad','ec','z','bc','bad','bav']
#words=['a','ad','ec','z','bc']
trie=make_trie_from_txtFile("english_words.txt")
#trie=make_trie(words)
#look('andtt',trie)
#look('ands',trie)
#look('finds',trie)
check=spell_check(trie)
check.spell_check('wront',2,10)
