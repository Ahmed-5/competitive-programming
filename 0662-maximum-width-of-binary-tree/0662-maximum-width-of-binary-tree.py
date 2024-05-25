from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(lambda: [None,None])
        m = 0
        
        s = [[1, 0, root]]
        
        while len(s)>0:
            v, h, n = s.pop()
            mi, ma = d[h]
            if mi:
                mi = min(v, mi)
            else:
                mi = v
                
            if ma:
                ma = max(v, ma)
            else:
                ma = v
                
            d[h] = [mi, ma]
            m = max(ma-mi+1, m)
            
            if n.left:
                s.append([2*v-1, h+1, n.left])
            
            if n.right:
                s.append([v*2, h+1, n.right])
            
        return m