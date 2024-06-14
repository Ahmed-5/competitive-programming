class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solved = False
        
        def solve(r=0, c=0):
            new_c = c+1
            new_r, new_c = r+int(new_c//9), new_c%9
            if r>=9 or self.solved:
                self.solved = True
                return
            
            if board[r][c] != ".":
                solve(new_r, new_c)
                return
            
            vals = [True for i in range(9)]
            rb, cb = r-(r%3), c-(c%3)
            for i in range(9):
                if board[r][i] != ".":
                    v = int(board[r][i])-1
                    vals[v] = False
                    
                if board[i][c] != ".":
                    v = int(board[i][c])-1
                    vals[v] = False
                
                dr, dc = int(i//3), i%3
                indr, indc = rb+dr, cb+dc
                if board[indr][indc] != ".":
                    v = int(board[indr][indc])-1
                    vals[v] = False
                    
            vals = [ind+1 for ind,i in enumerate(vals) if i]
            for i in vals:
                board[r][c] = str(i)
                solve(new_r, new_c)
                if self.solved:
                    return
                board[r][c] = "."
                
            
        solve()