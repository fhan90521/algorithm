class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail=ListNode(None),ListNode(None)
        self.size=k
        self.total=0
        self.head.right,self.tail.left=self.tail,self.head
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if(self.total<self.size):
            new=ListNode(value)
            new.left,new.right=self.head,self.head.right
            self.head.right.left,self.head.right=new,new
            self.total+=1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if(self.total<self.size):
            new=ListNode(value)
            new.left,new.right=self.tail.left,self.tail
            self.tail.left.right,self.tail.left=new,new
            self.total+=1
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if(self.total>0):
            self.head.right,self.head.right.left=self.head.right.right,self.head
            self.total-=1
            return True
        return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if(self.total>0):
            self.tail.left,self.tail.left.right=self.tail.left.left,self.tail
            self.total-=1
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if(self.total>0):
            return self.head.right.val
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if(self.total>0):
            return self.tail.left.val
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.total==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.total==self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()