# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [root1, root2]
        
        n1 = root1
        n2 = root2
        
        while n1 and n2 and len(s)>0:
            n2 = s.pop()
            n1 = s.pop()
            
            n1.val = n1.val + n2.val
            
            if n1.left and n2.left:
                s.append(n1.left)
                s.append(n2.left)
            elif not n1.left and n2.left:
                n1.left = n2.left
            
            if n1.right and n2.right:
                s.append(n1.right)
                s.append(n2.right)
            elif not n1.right and n2.right:
                n1.right = n2.right
                
        if root1:
            return root1
        
        return root2