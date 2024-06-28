class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        s = 0
        count = -1
        n = len(grid)
        visited = [[False for j in i] for i in grid]
        dirs = [[1, 0], [0, 1], [-1,0], [0,-1]]
        q = deque([])
        for i in range(n):
            for j in range(n):
                s += grid[i][j]
                if grid[i][j]==1:
                    q.append([i,j,0])
        
        if s==0 or s==n**2:
            return -1

        while len(q)>0:
            x,y,c = q.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            count = max(count, c)
            for dx, dy in dirs:
                x_, y_ = x+dx, y+dy
                if 0<=x_<n and 0<=y_<n and grid[x_][y_]==0:
                    q.append([x_, y_, c+1])

        return count
        