from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(lambda: [])

        if root is None:
            return []

        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
                
            if node.right:
                stack.append(node.right)
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)

        q = deque([[target.val, 0]])
        visited = defaultdict(lambda: False)
        nodes = []
        while len(q)>0:
            node, dist = q.popleft()
            if visited[node]:
                continue
            visited[node] = True
            if dist == k:
                nodes.append(node)

            for child in g[node]:
                q.append([child, dist+1])

        return nodes