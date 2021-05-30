class MyCircularQueue:

    def __init__(self, k: int):
        self.que=[None]*k
        self.size=k
        self.total=0
        self.back=-1
        self.front=0

    def enQueue(self, value: int) -> bool:
        if(self.total<self.size):
            self.total+=1
            self.back=(self.back+1)%self.size
            self.que[self.back]=value 
            
            return True
            
        return False

    def deQueue(self) -> bool:
        if(self.total>0):
            self.total-=1
            self.que[self.front]=None
            self.front=(self.front+1)%self.size
            
            return True
        return False

    def Front(self) -> int:
        if(self.total>0):
            return self.que[self.front]
        return -1    

    def Rear(self) -> int:
        if(self.total>0):
            
            return self.que[self.back]
        return -1

    def isEmpty(self) -> bool:
        return self.total==0

    def isFull(self) -> bool:
        return self.total==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()