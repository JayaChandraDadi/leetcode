class Solution(object):
    def path(self,i,j,matrix,n,dp):
        if j<0 or j>=n:
            return float('inf')
        if i==0:
            return matrix[0][j]
        if dp[i][j]!=0:
            return dp[i][j]
        down = matrix[i][j] + self.path(i-1,j,matrix,n,dp)
        leftdg = matrix[i][j] + self.path(i-1,j-1,matrix,n,dp)
        rightdg = matrix[i][j] + self.path(i-1,j+1,matrix,n,dp)
        dp[i][j] = min(down,leftdg,rightdg)
        return dp[i][j]
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        min1 = float('inf')
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                down = matrix[i][j]+ dp[i-1][j]
                if j-1>=0:
                    leftdg = matrix[i][j] + dp[i-1][j-1]
                else:
                    leftdg = float('inf')
                if j+1<n:
                    rightdg = matrix[i][j]+dp[i-1][j+1]
                else:
                    rightdg = float('inf')
                dp[i][j] = min(down,leftdg,rightdg)
        for i in range(n):
            min1 = min(min1,dp[n-1][i])
        return min1