# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        s1 = [(p, "root")]
        s2 = [(q, "root")]
        
        while len(s1)>0 and len(s2)>0:
            n1, t1 = s1.pop()
            n2, t2 = s2.pop()
            
            if n1 is None or n2 is None or n1.val != n2.val or t1 != t2:
                return False
            
            if n1.left:
                s1.append((n1.left, "left"))
            
            if n1.right:
                s1.append((n1.right, "right"))
            
            if n2.left:
                s2.append((n2.left, "left"))
            
            if n2.right:
                s2.append((n2.right, "right"))
                
        if len(s1) != len(s2):
            return False
        
        return True
        