# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        prev = None
        current = head
        
        while current:
            n = current.next
            # if n:
                # print("next", n.val)
            # else:
                # print("none next")
            s1 = None
            s2 = head
            s=0
            
            while s<l and s2.val < current.val:
                # print(s2, current)
                s += 1
                s1, s2 = s2, s2.next
                
            if s2 is current:
                # print("s2 is current", s2.val)
                prev = current
                # print("new prev", prev.val)
            else:
                if prev:
                    # print("prev", prev.val)
                    prev.next = n
                # print("current", current.val)
                if s==0:
                    current.next, head = head, current
                    # print("new head", head.val)
                else:
                    # print("s1", s1.val)
                    s1.next = current
                    current.next = s2
                    s2 = current
                
                while s<l:
                    s += 1
                    s1, s2 = s2, s2.next
                
                if s2 and (not prev or s2.val>prev.val):    
                    prev = s2
                    # print("new prev", prev.val)
                    
            current = n
            l+=1
                
        return head