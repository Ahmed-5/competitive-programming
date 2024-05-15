# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = self.traverse(root)
        return nodes
    
    def traverse(self, node):
        if node:
            left = self.traverse(node.left)
            left.append(node.val)
            right = self.traverse(node.right)
            left.extend(right)
            return left
        else:
            return []
        