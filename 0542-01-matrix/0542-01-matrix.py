class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        visited = [[-1 for j in i] for i in mat]
        dirs = [[1, 0], [0, 1], [-1,0], [0,-1]]
        q = deque([])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append([i,j,0])

        while len(q)>0:
            x,y,c = q.popleft()
            if visited[x][y] != -1:
                continue
            visited[x][y] = c
            for dx, dy in dirs:
                x_, y_ = x+dx, y+dy
                if 0<=x_<n and 0<=y_<m and mat[x_][y_]==1:
                    q.append([x_, y_, c+1])

        return visited
        