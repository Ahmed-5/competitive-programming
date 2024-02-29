class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        
        d = m+n-1
        ds = []
        
        f = True
        x = 0
        y = 0
        s = 0
        for i in range(d):
            ds.append([])
            while -1<x<n and -1<y<m:
                ds[-1].append(mat[x][y])
                if f:
                    x-=1
                    y+=1
                else:
                    x+=1
                    y-=1
            if f:
                x += 1
                if y>m-1:
                    y = m-1
                    x += 1
            else:
                y += 1
                if x>n-1:
                    x = n-1
                    y += 1
                    
            f = not f
            
        ds = [j for i in ds for j in i]
        return ds