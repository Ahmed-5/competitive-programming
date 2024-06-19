# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node, pv=1, gpv=1):
            if not node.left and not node.right:
                return (1-(gpv%2))*node.val
            
            
            temp = (1-(gpv%2))*node.val
            if node.right:
                temp += dfs(node.right, node.val, pv)
            if node.left:
                temp += dfs(node.left, node.val, pv)
                
            return temp
        
        return dfs(root)
        