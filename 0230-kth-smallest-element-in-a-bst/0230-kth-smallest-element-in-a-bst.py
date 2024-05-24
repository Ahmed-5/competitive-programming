# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        arr = []
        current = root
        
        while len(arr)<k:
            if current:
                s.append(current)
                current = current.left
                
            elif len(s)>0:
                current = s.pop()
                arr.append(current.val)
                current = current.right
                    
            else:
                break
                    
                    
        return arr[-1]
            
        