# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        v1 = p.val
        v2 = q.val
        v1, v2 = min(v1, v2), max(v1, v2)
        
        n = root
        while n is not None:
            v = n.val
            if v == v1 or v == v2:
                return n
            
            if v1<v<v2:
                return n
            
            if v2<v:
                n = n.left
                
            if v<v1:
                n = n.right
                
            