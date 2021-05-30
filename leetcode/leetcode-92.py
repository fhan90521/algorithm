# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        current=head
        prev=None 
        if(m==1):
            i=1
            while(i<=n):
                if(i==n):
                    root=current
                current.next,current,prev=prev,current.next,current
                i+=1
            if(current):
                head.next=current    
            return root
        else:
            i=1
            while(i<m):
                current,prev=current.next,current
                i+=1
            before_m=prev
            m_th=current
            prev=None
            while(m<=i and i<=n):
                if(i==n):
                    root=current
                current.next,current,prev=prev,current.next,current
                i+=1
            if(current):
                m_th.next=current
            before_m.next=root
            return head