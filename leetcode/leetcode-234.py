# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head==None):return True
        val_list=[]
        while(True):
            val_list.append(head.val)
            if(head.next==None):
                break
            head=head.next
        
        if(val_list==val_list[::-1]):
            return True
        else:
            return False