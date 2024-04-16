# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        i = head
        arr = []
        
        while i:
            arr.append(i.val)
            i = i.next
            
        n = len(arr)
        n2 = int(n//2)
        for i in range(n2):
            if arr[i] != arr[-i-1]:
                return False
            
        return True
        