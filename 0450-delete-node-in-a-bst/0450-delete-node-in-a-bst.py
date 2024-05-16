# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        parent = None
        direction = True
        while node is not None:
            if node.val == key:
                break
            elif node.val > key:
                parent = node
                direction = False
                node = node.left
            else:
                parent = node
                direction = True
                node = node.right
                
        if node is None:
            return root
        
        next_node = node.right
        while next_node and next_node.left:
            next_node = next_node.left
            
        if next_node is None:
            next_node = node.left
            while next_node and next_node.right:
                next_node = next_node.right
         
        if next_node is None:
            if parent is None:
                root = None
                return root
            
            if direction:
                parent.right = None
            else:
                parent.left = None
                
            return root
        
        v = next_node.val
        self.deleteNode(root, next_node.val)
        node.val = v
        
        return root
        
                
        
        