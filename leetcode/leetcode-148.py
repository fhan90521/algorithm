# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        current= head
        node_list=[]
        while current:
            node_list.append(current.val)
            current=current.next
        node_list.sort()
        current=head
        for i in range(len(node_list)):
            current.val = node_list[i]
            current= current.next
        return head