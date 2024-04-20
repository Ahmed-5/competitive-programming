# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        current = l1
        while current:
            s1.append(str(current.val))
            current = current.next
        
        s2 = []
        current = l2
        while current:
            s2.append(str(current.val))
            current = current.next
            
        i1 = int("".join(s1))
        i2 = int("".join(s2))
        
        i3 = i1+i2
        i3 = [int(i) for i in str(i3)]
        
        head = None
        if len(i3)>0:
            head = ListNode(i3[0])
            current = head
            for i in i3[1:]:
                node = ListNode(i)
                current.next = node
                current = node
                
        return head