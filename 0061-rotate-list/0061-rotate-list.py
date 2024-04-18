# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        last = None
        current = head
        while current:
            last, current = current, current.next
            l += 1
        
        if l == 0:
            return None
        
        rots = k%l
        ind = l-rots
        
        if rots == 0:
            return head
        
        prev = None
        current = head
        for i in range(ind):
            prev, current = current, current.next
            
        prev.next = None
        last.next = head
        head = current
        
        return head
            