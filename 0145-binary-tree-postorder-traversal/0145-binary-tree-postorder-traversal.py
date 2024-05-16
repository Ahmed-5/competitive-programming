# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root)
    
    def traverse(self, node):
        if node is None:
            return []
        
        left = self.traverse(node.left)
        left.extend(self.traverse(node.right))
        left.append(node.val)
        
        return left
        