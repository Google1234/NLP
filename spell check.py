#-*- coding: UTF-8 -*-
class quick_sort():
    a=[]
    def __init__(self,data):
        self.a=data[:]
    def sort(self,left,right):
        if left!=right:
            mid=left+int((right-left)/2)
            self.sort(left,mid)
            self.sort(mid+1,right)
            b=[]
            i=0
            for i in range(left,mid+1):
                b.append(self.a[i])
            b.append('zz')
            i=0
            for i in range(mid+1,right+1):
                b.append(self.a[i])
            b.append('zz')

            i=j=0
            k=mid-left+2
            for i in range(left,right+1):
                if b[j]>b[k]:
                    value=b[k]
                    k+=1
                else:
                    value=b[j]
                    j+=1
                self.a[i]=value
        return self.a
    def show(self):
        print(self.a)
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



words=['a','ad','ec','z','bc']
trie=make_trie_from_txtFile("english_words.txt")
look('andtt',trie)
look('ands',trie)
look('finds',trie)

