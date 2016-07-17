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
class quick_sort_Multidimensional_Data():
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
            b.append(['',10])
            i=0
            for i in range(mid+1,right+1):
                b.append(self.a[i])
            b.append(['',10])

            i=j=0
            k=mid-left+2
            for i in range(left,right+1):
                if b[j][0]>b[k][0]:
                    value=b[k]
                    k+=1
                else:
                    value=b[j]
                    j+=1
                self.a[i]=value
        return self.a
    def show(self):
        print(self.a)