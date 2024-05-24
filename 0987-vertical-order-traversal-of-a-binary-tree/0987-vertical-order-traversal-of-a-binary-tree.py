from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = [[0, 0, root]]
        d = defaultdict(list)
        
        while len(s)>0:
            v, h, n = s.pop()
            d[v].append([h, n.val])
            
            if n.left:
                s.append([v-1, h+1, n.left])
                
            if n.right:
                s.append([v+1, h+1, n.right])
            
            
        k = list(d.keys())
        k.sort()
        
        arr = []
        for i in k:
            l = d[i]
            l.sort()
            l = [j[1] for j in l]
            arr.append(l)
            
        return arr