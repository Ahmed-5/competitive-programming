# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            if prev and current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev, current = current, current.next
                
        return head
        