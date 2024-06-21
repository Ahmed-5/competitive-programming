class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0
        visited = [[False for j in i] for i in grid]
        
        def visit_island(x,y):
            if grid[x][y] == "0":
                return
            
            self.islands += 1
            stack = [[x,y]]
            dirs = [[-1,0], [0,-1], [1,0], [0,1]]
            while len(stack) > 0:
                x,y = stack.pop()
                visited[x][y] = True
                for dx, dy in dirs:
                    new_x, new_y = x+dx, y+dy
                    if -1<new_x<len(grid) and -1<new_y<len(grid[0]) and not visited[new_x][new_y] and grid[new_x][new_y]=="1":
                        stack.append([new_x, new_y])
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    visit_island(i, j)
                        
        return self.islands