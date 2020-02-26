class Stack:
    def __init__(self,size=50):
        self.ds=[]
        self.top=-1
        self.size=size
        #print("size stack with size {} has been created".format(self.size))
    def push(self,element):
        if self.top==self.size-1:
            print("Overflow")
            return 0
        else:
            self.ds.append(element)
            self.top+=1
    #def top(self):
    #    return self.ds[-1]
    def pop(self):
        if self.top==-1:
            #print("Underflow")
            return 0
        else:
            x=self.ds[self.top]
            del self.ds[self.top]
            self.top-=1
            return x
    def show(self):
        print("*****Stack*****")
        for i in range(self.top,-1,-1):
            print(self.ds[i])
            