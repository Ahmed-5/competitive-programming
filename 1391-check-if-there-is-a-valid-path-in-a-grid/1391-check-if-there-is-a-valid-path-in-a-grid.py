class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        cells = [
            None,
            [0,2],
            [1,3],
            [0,3],
            [2,3],
            [0,1],
            [1,2],
        ]
        
        dirs = [
            [ 0, -1],
            [-1,  0],
            [ 0,  1],
            [ 1,  0],
        ]
        
        n = len(grid)
        m = len(grid[0])
        stack = [([0,0], None)]
        
        visited = []
        for i in grid:
            visited.append([])
            for j in i:
                visited[-1].append(False)
        
        while len(stack) != 0:
            cell, direction = stack.pop()
            i, j = cell
            if visited[i][j]:
                continue
            
            typ = grid[i][j]
            availble_dirs = cells[typ]
            if direction is not None and direction not in availble_dirs:
                continue
                
            visited[i][j] = True
            if i==n-1 and j==m-1:
                return True
                
            for d in availble_dirs:
                if d == direction:
                    continue
                new_direction = (2+d)%4
                new_i, new_j = i+dirs[d][0], j+dirs[d][1]
                if 0<=new_i<n and 0<=new_j<m:
                    stack.append(([new_i, new_j], new_direction))