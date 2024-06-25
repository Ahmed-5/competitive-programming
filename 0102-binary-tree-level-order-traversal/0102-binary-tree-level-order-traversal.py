from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        levels = []
        q = deque([(root, 0)])
        
        while len(q)>0:
            node, level = q.pop()
            if len(levels)<=level:
                while len(levels)<=level:
                    levels.append([])
            levels[level].append(node.val)
            
            if node.left:
                q.appendleft((node.left, level+1))
            if node.right:
                q.appendleft((node.right, level+1))
            
        return levels
                