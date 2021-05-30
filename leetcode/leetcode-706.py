class ListNode:
    def __init__(self,key=None, value=None):
        self.key=key
        self.value=value
        self.next=None
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=1000
        self.table=[ListNode(None)]*1000
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key%1000
        if self.table[index].value is None:
            self.table[index]=ListNode(key,value)
            return
        p=self.table[index]
        while p:
            if p.key==key:
                p.value=value
                return
            if p.next is None:
                break
            p=p.next
        p.next=ListNode(key,value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key%self.size
        if(self.table[index].value is None):
            return -1
        p=self.table[index]
        while p:
            if p.key==key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key%self.size
        if self.table[index].value is None:
            return
        
        p=self.table[index]
        if p.key==key:
            self.table[index]=ListNode() if p.next is None else p.next
            return
        prev =p
        while p:
            if p.key==key:
                prev.next=p.next
                return
            prev,p=p,p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)