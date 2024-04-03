from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        s = []
        for i in range(n):
            s.append([0])
            for j in range(m):
                s[-1].append(s[-1][-1]+ matrix[i][j])
            
        count = 0
        
        
        for j in range(m):
            for k in range(j+1, m+1):
                summ = 0
                ds = defaultdict(int)
                ds[0] = 1
                for i in range(n):
                    summ += s[i][k] - s[i][j]
                    # print(summ)
                    diff = summ - target
                    if diff in ds:
                        count += ds[diff]
                    ds[summ] += 1
                
        return count