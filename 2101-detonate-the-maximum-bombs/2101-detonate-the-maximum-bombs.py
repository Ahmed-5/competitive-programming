from math import sqrt

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def isIntersected(circle1, circle2):
            x1, y1, r1 = circle1
            x2, y2, r2 = circle2
            dist = sqrt((x1-x2)**2 + (y1-y2)**2)
            return r1>=dist, r2>=dist
        
        n = len(bombs)
        graph = [[0 for j in range(n)] for i in range(n)]
            
        for i in range(n):
            for j in range(i, n):
                circle1 = bombs[i]
                circle2 = bombs[j]
                outwards, inwards = isIntersected(circle1, circle2)
                if outwards:
                    graph[i][j] = 1
                if inwards:
                    graph[j][i] = 1
                    
        for i in range(n):
            for j in range(n):
                if j==i or (graph[i][j]==0 and graph[j][i]==0):
                    continue
                    
                if graph[j][i]==1:
                    for k in range(n):
                        if graph[i][k]==1:
                            graph[j][k]=1
                    
                if graph[i][j]==1:
                    for k in range(n):
                        if graph[j][k]==1:
                            graph[i][k]=1
                            
        intersections = [sum(i) for i in graph]
            
        return max(intersections)