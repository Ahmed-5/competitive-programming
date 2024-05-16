# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        parent = None
        while node is not None:
            if node.val == val:
                return node
            elif node.val > val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
                
        newNode = TreeNode(val)
        if parent is None:
            root = newNode
        elif parent.val > val:
            parent.left = newNode
        else:
            parent.right = newNode
            
        return root