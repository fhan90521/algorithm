# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1==None):return l2
        if(l2==None):return l1
        
        if(l1.val<l2.val):
            head=l1
            l1_current=l1.next
            l2_current=l2
        else:
            head=l2
            l1_current=l1
            l2_current=l2.next
        current=head
      
        while(True):
            if(l1_current==None and l2_current==None):
                break
            if(l1_current==None):
                current.next=l2_current
                current=current.next
                l2_current=l2_current.next
                continue
            if(l2_current==None):
                current.next=l1_current
                current=current.next
                l1_current=l1_current.next
                continue
            if(l1_current.val<l2_current.val):
                current.next=l1_current
                current=current.next
                l1_current=l1_current.next
            else:
                current.next=l2_current
                current=current.next
                l2_current=l2_current.next
        return head