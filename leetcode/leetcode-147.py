# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if(head==None): return
        current=head.next
        tail=head
        while current:

            sort_current=head.next
            prefer=head
            if(current.val<=head.val):
                current.next,tail.next,head,current=head,current.next,current,current.next
                continue
            if(current.val>=tail.val):
                tail=current
                current=current.next
                continue
    
            while True:
        
                if(current.val<sort_current.val):
                    current.next,current,prefer.next,tail.next=sort_current,current.next,current,current.next
                    break
                if(sort_current==tail):break
                sort_current=sort_current.next
                prefer=prefer.next
            
                    
        return head
            