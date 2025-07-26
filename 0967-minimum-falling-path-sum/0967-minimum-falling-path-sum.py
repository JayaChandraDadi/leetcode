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
        temp = [0]*n
        for i in range(n):
            temp[i] = matrix[0][i]
        prev = temp
        for i in range(1,n):
            temp = [0]*n
            for j in range(n):
                down = matrix[i][j]+ prev[j]
                if j-1>=0:
                    leftdg = matrix[i][j] + prev[j-1]
                else:
                    leftdg = float('inf')
                if j+1<n:
                    rightdg = matrix[i][j]+prev[j+1]
                else:
                    rightdg = float('inf')
                temp[j] = min(down,leftdg,rightdg)
            prev = temp
        
        return min(prev)