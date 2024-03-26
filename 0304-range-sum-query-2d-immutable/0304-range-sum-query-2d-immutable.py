class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ranges = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            self.ranges.append([0])
            for j in range(m):
                current = self.ranges[i][j] + matrix[i][j]
                if i>0:
                    current += self.ranges[i-1][j+1]-self.ranges[i-1][j]
                    
                self.ranges[-1].append(current)
                
        for i in self.ranges:
            print(*i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.ranges[row2][col2+1] - self.ranges[row2][col1]
        if row1>0:
            s -= self.ranges[row1-1][col2+1]
            s += self.ranges[row1-1][col1]
            
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)