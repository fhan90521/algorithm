# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None):return head
        before=head
        head=after=head.next
        while(True):
            if(after.next==None):
                before.next,after.next=None,before
                break
            if(after.next.next==None):
                before.next,after.next=after.next,before
                break
            before.next,after.next,before,after=after.next.next,before,after.next,after.next.next
           
        return head