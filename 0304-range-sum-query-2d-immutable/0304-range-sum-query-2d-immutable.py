class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.prefix = [[0]*(n) for _ in range(m)]
        sum1 = 0
        for i in range(m):
            sum1+=matrix[i][0]
            self.prefix[i][0] = sum1
        sum1 = 0
        for j in range(n):
            sum1+=matrix[0][j]
            self.prefix[0][j] = sum1
        for i in range(1,m):
            for j in range(1,n):
                self.prefix[i][j] = self.prefix[i][j-1] + self.prefix[i-1][j] - self.prefix[i-1][j-1] + matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        leftprefix = 0
        rightprefix = 0
        previous = 0
        if col1-1>=0:
            leftprefix = self.prefix[row2][col1-1]
        if row1-1>=0:
            rightprefix = self.prefix[row1-1][col2]
        if row1>0 and col1>0:
            previous = self.prefix[row1-1][col1-1]
        return self.prefix[row2][col2] - leftprefix - rightprefix + previous
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)