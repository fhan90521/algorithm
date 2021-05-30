# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num=1
        sum_l1=0
        while(l1):
            sum_l1+=l1.val*num
            num*=10
            l1=l1.next
        num=1
        sum_l2=0
        while(l2):
            sum_l2+=l2.val*num
            num*=10
            l2=l2.next
        total=sum_l1+sum_l2
        total=str(total)
        head=ListNode(int(total[-1]))
        current=head
        for i in range(len(total)-2,-1,-1):
            node=ListNode(int(total[i]))
            current.next=node
            current=current.next
        return head
