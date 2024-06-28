from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n = len(maze)
        m = len(maze[0])

        q = deque([[*entrance, 0]])

        while len(q)>0:
            x, y, count = q.popleft()
            if maze[x][y] == "+":
                continue
            elif (x==0 or x==n-1 or y==0 or y==m-1) and not(x == entrance[0] and y==entrance[1]):
                return count
            maze[x][y] = "+"

            for dx, dy in dirs:
                x_, y_ = x+dx, y+dy
                if 0<=x_<n and 0<=y_<m and maze[x_][y_] == ".":
                    q.append([x_, y_, count+1])

        return -1