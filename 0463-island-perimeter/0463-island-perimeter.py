class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        
        sides = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        x, y = i+dx, j+dy
                        if x<0 or y<0 or x>=len(grid) or y>=len(grid[i]) or grid[x][y] == 0:
                            sides += 1
                            
        return sides