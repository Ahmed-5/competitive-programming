# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        l = []
        
        while current:
            l.append(current)
            current = current.next
            
        l.reverse()
        n_l = len(l)
        if n_l == 1:
            head = None
        elif n == n_l:
            head = l[-2]
        else:
            l[n].next = l[n-1].next
        
        return head
        