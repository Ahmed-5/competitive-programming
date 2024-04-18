# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = l1
        s2 = l2
        
        carry = 0
        
        l3 = None
        last = None
        
        while s1 and s2:
            v = s1.val + s2.val + carry
            carry = int(v//10)
            v = v%10
            node = ListNode(v)
            if not l3:
                l3 = node
            if last:
                last.next = node
            last = node
            
            s1 = s1.next
            s2 = s2.next
            
        while s1:
            v = s1.val + carry
            carry = int(v//10)
            v = v%10
            node = ListNode(v)
            if not l3:
                l3 = node
            last.next = node
            last = node
            
            s1 = s1.next
            
        while s2:
            v = s2.val + carry
            carry = int(v//10)
            v = v%10
            node = ListNode(v)
            if not l3:
                l3 = node
            last.next = node
            last = node
            
            s2 = s2.next
            
        if carry == 1:
            node = ListNode(carry)
            last.next = node
            last = node
            
        return l3