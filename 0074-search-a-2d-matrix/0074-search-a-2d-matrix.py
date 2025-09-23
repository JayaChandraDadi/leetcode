class Solution(object):
    def searchMatrix(self, matrix, target):
        m  = len(matrix)
        n = len(matrix[0]) if m else 0
        row = 0
        col = n-1
        while(row<m and col>=0):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False