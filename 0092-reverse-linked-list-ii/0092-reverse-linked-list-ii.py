# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = None
        suf = None
        i=1
        current = head
        prev = None
        
        while current:
            if left<i<right:
                prev, current.next, current = current, prev, current.next
            elif i == left:
                pre = prev
                prev, current = current, current.next
            elif i == right:
                suf = current
                if pre is not None and pre.next:
                    pre.next.next = current.next
                    pre.next = current
                else:
                    head.next = current.next
                    head = current
                prev, current.next, current = current, prev, current.next
            else:
                prev, current = current, current.next
            
            i+=1
                
        return head
    