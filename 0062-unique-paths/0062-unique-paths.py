class Solution(object):
    def path(self,i,j,dp):
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up = self.path(i-1,j,dp)
        left = self.path(i,j-1,dp)
        dp[i][j] = up+left
        return dp[i][j]    
    def uniquePaths(self, m, n):
        prev = [0]*n 
        for i in range(m):
            temp = [0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[j] = 1
                else:
                    temp[j] = prev[j]+temp[j-1]
            prev= temp
        return prev[n-1]