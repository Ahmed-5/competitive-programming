# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        start = head
        current = head
        for i in range(n):
            current = current.next
            if not current:
                break
            
        while current:
            prev, start = start, start.next
            current = current.next
            
        if start is head:
            head = start.next
        else:
            prev.next = start.next
            
        return head