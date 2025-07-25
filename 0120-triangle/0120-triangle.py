class Solution(object):
    def path(self,i,j,m,triangle,dp):
        if i==m-1:
            return triangle[i][j]
        if dp[i][j]!=0:
            return dp[i][j]
        down = triangle[i][j] + self.path(i+1,j,m,triangle,dp)
        dg = triangle[i][j] + self.path(i+1,j+1,m,triangle,dp)
        dp[i][j] =  min(down,dg)
        return dp[i][j]
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp =  [[0]*n for _ in range(n)]
        temp = [0]*n
        for j in range(n):
            temp[j] = triangle[n-1][j]
        prev = temp
        for i in range(n-2,-1,-1):
            temp = [0]*(i+1)
            for j in range(i,-1,-1):
                down = triangle[i][j] + prev[j]
                dg = triangle[i][j] + prev[j+1]
                temp[j] = min(down,dg)
            prev = temp
        return prev[0]
        