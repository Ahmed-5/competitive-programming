# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node:
            left = self.traverse(node.left)
            left.append(node.val)
            right = self.traverse(node.right)
            left.extend(right)
            return left
        else:
            return []
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.traverse(root)
        def BST(start, end):
            mid = int(start+end)//2
            v = nums[mid]
            
            node = TreeNode(v)
            if mid<end:
                node.right = BST(mid+1, end)
            if mid>start:
                node.left = BST(start, mid-1)
            
            
            return node
        
        return BST(0, len(nums)-1)