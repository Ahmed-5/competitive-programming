# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, val=0):
            new_val = val*10 + node.val
            if not node.left and not node.right:
                return new_val
            
            temp = 0
            if node.right:
                temp += dfs(node.right, new_val)
            if node.left:
                temp += dfs(node.left, new_val)
                
            return temp
        
        return dfs(root)