from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        num_rotten = 0
        num_rotted = 0
        n = len(grid)
        m = len(grid[0])
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        max_t = 0
        
        parents = []
        q = deque([])
        for indr, r in enumerate(grid):
            parents.append([])
            for indc, c in enumerate(r):
                parents[-1].append(-1)
                if c==1:
                    num_fresh += 1
                elif c==2:
                    num_rotten += 1
                    q.append([indr, indc, 0])
                
        while len(q)>0:
            r,c,t = q.popleft()
            if parents[r][c] != -1 or grid[r][c] == 0:
                continue
                
            if grid[r][c] == 1:
                num_rotted += 1
                
            parents[r][c] = t
            max_t = max(max_t, t)
            for dx, dy in dirs:
                rr = r+dx
                cc = c+dy
                if 0<=rr<n and 0<=cc<m:
                    q.append([rr,cc,t+1])
                    
        if num_rotted != num_fresh:
            return -1
        
        return max_t