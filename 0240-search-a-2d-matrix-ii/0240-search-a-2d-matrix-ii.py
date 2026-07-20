class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        row = 0
        n = len(matrix[0]) if m else 0
        col = n-1
        while(row<m and col>=0):
            if matrix[row][col] == target:
                return True
            if matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False