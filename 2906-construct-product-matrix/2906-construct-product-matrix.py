class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        l = []
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                l.append(grid[i][j])
                
        prefix = [1]
        for i in l:
            p = prefix[-1]*i
            p = p%12345
            prefix.append(p)
            
        l.reverse()
        suffix = [1]
        for i in l:
            p = suffix[-1]*i
            p = p%12345
            suffix.append(p)
            
        suffix.reverse()
            
        mat = []
        for i in range(n):
            mat.append([])
            for j in range(m):
                ind = i*m + j
                p = (prefix[ind]*suffix[ind+1])%12345
                mat[-1].append(p)
                
        return mat
                
        