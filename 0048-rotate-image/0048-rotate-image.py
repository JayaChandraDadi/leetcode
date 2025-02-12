class Solution(object):
    def rotate(self, matrix):
        m = len(matrix)
        n= len(matrix[0]) if matrix else 0
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(m):
            matrix[i].reverse()
        return matrix
        