# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = [(None, None, root)]
            
        while len(s)>0:
            l, r, n = s.pop()
            
            if l is not None:
                if n.val <= l:
                    return False
            if r is not None:
                if n.val >= r:
                    return False
            
            if n.left:
                s.append((l ,n.val ,n.left))
            if n.right:
                s.append((n.val ,r ,n.right))
        
        return True