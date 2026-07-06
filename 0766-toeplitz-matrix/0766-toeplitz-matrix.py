class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    continue
                elif matrix[i-1][j-1]!=matrix[i][j]:
                    return False
        return True