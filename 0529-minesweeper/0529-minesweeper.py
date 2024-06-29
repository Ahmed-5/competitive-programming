from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        q = deque([click])
        n = len(board)
        m = len(board[0])
        dirs = [
            [0,1], [0,-1],
            [1,1], [1,-1], [1, 0],
            [-1,1], [-1,-1], [-1, 0]
        ]

        while len(q)>0:
            x, y = q.popleft()
            if board[x][y] not in ["E", "M"]:
                continue

            if board[x][y] == "M":
                board[x][y] = "X"

            elif board[x][y] == "E":
                mines = 0
                for dx, dy in dirs:
                    i, j = x+dx, y+dy
                    if 0<=i<n and 0<=j<m and board[i][j] in ["M", "X"]:
                        mines += 1
                board[x][y] = "B" if mines == 0 else str(mines)

            if board[x][y] != "B":
                continue

            for dx, dy in dirs:
                i, j = x+dx, y+dy
                if 0<=i<n and 0<=j<m and board[i][j] == "E":
                    q.append([i,j])

        for i in board:
            print(*i)

        return board
