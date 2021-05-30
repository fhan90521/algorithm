class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]
        self.size=0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp=[]
        for i in range(self.size):
            temp.append(self.queue.pop())
        temp.append(x)
        self.size+=1
        queue=[]
        for i in range(self.size):
            queue.append(temp.pop())
        self.queue=queue
        
            
            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size-=1
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[self.size-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()