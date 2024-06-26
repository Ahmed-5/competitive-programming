# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = []
        val = root.val
        
        q.append(root)
        while len(q)>0:
            node = q.pop()
            if node.val != val:
                return False
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        return True
        