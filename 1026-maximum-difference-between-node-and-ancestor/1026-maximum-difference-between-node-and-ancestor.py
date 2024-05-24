# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        m = 0
        s = [(root.val, root.val, root)]
        
        while len(s)>0:
            mi, ma, n = s.pop()
            m = max(m ,ma - mi)
                
            if n.left:
                mi2 = min(mi, n.left.val)
                ma2 = max(ma, n.left.val)
                s.append((mi2, ma2, n.left))
                
            if n.right:
                mi2 = min(mi, n.right.val)
                ma2 = max(ma, n.right.val)
                s.append((mi2, ma2, n.right))
                
        return m