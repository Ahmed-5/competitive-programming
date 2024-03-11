class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        
        mat = []
        for j in range(m):
            mat.append([])
            for i in range(n):
                mat[-1].append(matrix[i][j])
                
        return mat
        