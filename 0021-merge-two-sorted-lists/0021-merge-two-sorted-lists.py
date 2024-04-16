# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i1 = list1
        i2 = list2
        
        i1_ = None
        i2_ = None
        
        while i1 is not None and i2 is not None:
            if i1.val<i2.val:
                while i1 is not None and i1.val<=i2.val:
                    i1_, i1 = i1, i1.next
                i1_.next = i2
            else:
                while i2 is not None and i2.val<=i1.val:
                    i2_, i2 = i2, i2.next
                i2_.next = i1
                
        if list1 is not None and (list2 is None or list1.val<list2.val):
            return list1
        return list2