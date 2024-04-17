# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        turtle = head
        
        while hare is not None and turtle is not None:
            if hare.next:
                hare = hare.next.next
            else:
                break
            turtle = turtle.next
            
            if hare is turtle:
                return True
            
        return False