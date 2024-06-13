import sys
from collections import defaultdict

input = sys.stdin.readline

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parents = [0 for i in range(n)]
        
        for i, j in edges:
            parents[j] += 1
            
        l = []
        for i in range(n):
            if parents[i] == 0:
                l.append(i)
                
        return l
        
        