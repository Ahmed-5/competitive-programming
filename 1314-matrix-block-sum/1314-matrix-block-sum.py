class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        s = [[0 for _ in range(m+1)]]
        for i in range(1, n+1):
            s.append([0])
            for j in range(m):
                val = s[i][j] + mat[i-1][j]
                val += s[i-1][j+1] - s[i-1][j]
                s[-1].append(val)
                
        # for i in s:
        #     print(i)
                
        matrix = []
        for i in range(1, n+1):
            matrix.append([])
            for j in range(1, m+1):
                si = max(0, i-k-1)
                sj = max(0, j-k-1)
                ei = min(n, i+k)
                ej = min(m, j+k)
                
                val = s[ei][ej] + s[si][sj]
                val -= s[si][ej] + s[ei][sj]
                matrix[-1].append(val)
                
        # print()
        # for i in matrix:
        #     print(i)
        return matrix