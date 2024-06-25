from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([])
        val = root.val
        
        q.appendleft(root)
        while len(q)>0:
            node = q.pop()
            if node.val != val:
                return False
            
            if node.left:
                q.appendleft(node.left)
                
            if node.right:
                q.appendleft(node.right)
                
        return True
        