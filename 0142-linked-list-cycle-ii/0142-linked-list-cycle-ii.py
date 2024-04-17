# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        turtle = head
        
        while hare is not None and turtle is not None:
            if hare.next:
                hare = hare.next.next
            else:
                break
            turtle = turtle.next
            
            if hare is turtle:
                hare = head
                while hare is not turtle:
                    hare = hare.next
                    turtle = turtle.next
                    
                return hare
            
        return None