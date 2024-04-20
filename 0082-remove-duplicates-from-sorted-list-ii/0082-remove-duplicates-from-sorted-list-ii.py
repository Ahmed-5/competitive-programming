# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = None
        prev2 = None
        prev = None
        current = head
        
        while current:
            if prev and current.val == prev.val:
                if not prev2:
                    s = "head"
                elif prev2.val != prev.val:
                    s = prev2
                prev2, prev, current = prev, current, current.next
            elif s:
                if s == "head":
                    head = current
                    prev2, prev, current = None, current, current.next
                else:
                    s.next = current
                    prev2, prev, current = s, current, current.next
                s = None
            else:
                prev2, prev, current = prev, current, current.next
        
        if s == "head":
            head = None
        elif s:
            s.next = None
        return head