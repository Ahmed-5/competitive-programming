class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        sol = []
        for i in range(n):
            sol.append([])
            for j in range(n):
                sol[-1].append(".")
                
        def placable(n, r, c):
            for i in range(n):
                if sol[i][c] == "Q" or sol[r][i]=="Q":
                    return False
                
                if c-i>-1 and r-i>-1 and sol[r-i][c-i]=="Q":
                    return False
                
                if c-i>-1 and r+i<n and sol[r+i][c-i]=="Q":
                    return False
                
                if c+i<n and r-i>-1 and sol[r-i][c+i]=="Q":
                    return False
                
                if c+i<n and r+i<n and sol[r+i][c+i]=="Q":
                    return False
                
            return True
        
        def solve(n, r=0):
            if r==n:
                added = ["".join(i) for i in sol]
                ans.append(added)
                return
            
            placed = True
            for c in range(n):
                placed = placable(n, r, c)
                if not placed:
                    continue
                    
                sol[r][c] = "Q"
                solve(n, r+1)
                sol[r][c] = "."
            
        solve(n)
        
        return ans