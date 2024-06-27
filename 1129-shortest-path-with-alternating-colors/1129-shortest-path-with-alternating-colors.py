from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        
        for i, j in redEdges:
            g[i].append([j, 0, False])
        
        for i, j in blueEdges:
            g[i].append([j, 1, False])
            
        q = deque([(0, 0, None)])
        path = [-1 for i in range(n)]
        
        while len(q)>0:
            node, cost, color = q.popleft()
            # if path[node] != -1:
            #     continue
                
            if path[node] == -1:
                path[node] = cost
            for ind, edge in enumerate(g[node]):
                child, c, visited = edge
                if (color is None or c==1-color) and not visited:
                    g[node][ind][2] = True
                    q.append((child, cost+1, c))
                    
        return path