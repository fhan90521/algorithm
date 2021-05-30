# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None): return head
        current=head.next
        odd=head
        even_head=None
        even=None
        i=2
        while(current):
            if(i==2):
                even_head=current
                even=current
            if(i%2==1):
                odd.next=current
                odd=current
            if(i%2==0 and i>2):
                even.next=current
                even=current
            current=current.next
            i+=1
        if(even):even.next=None
        odd.next=even_head
    
        
        return head