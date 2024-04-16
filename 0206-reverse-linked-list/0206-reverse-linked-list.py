# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i1 = head
        i2 = None
        
        while i1:
            i1.next, i1, i2 = i2, i1.next, i1
            
        return i2