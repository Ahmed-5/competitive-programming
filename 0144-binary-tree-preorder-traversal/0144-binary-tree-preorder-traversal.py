# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        if root:
            l = [root.val]
            if root.right:
                s.append(root.right)
            if root.left:
                s.append(root.left)
        else:
            return []
        
        n = root
        while len(s)>0:
            n = s.pop()
            l.append(n.val)
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)
                
                
        return l