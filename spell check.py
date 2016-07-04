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
    pointer=0
    value='#'         #size =size of words
    child_pointer=0   #size = 4
    next_pointer=0    #size = 4
    buff=[]
    buff.append([value,child_pointer,next_pointer])
    pointer+=1
    #run
    for word in words:
        last_value=buff[pointer-1][0]

    return 0

words=['a','ad','ec','z','bc']
make_trie(words)

