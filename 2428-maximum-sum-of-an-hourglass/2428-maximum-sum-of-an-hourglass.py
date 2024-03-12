class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_hour = 0
        
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n-2):
            for j in range(m-2):
                hour = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                max_hour = max(max_hour, hour)
                
                
        return max_hour
        