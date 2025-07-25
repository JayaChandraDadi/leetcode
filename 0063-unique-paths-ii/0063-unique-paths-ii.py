class Solution(object):
    def paths(self,i,j,mat,dp):
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if i>=0 and j>=0 and mat[i][j]==1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        left = self.paths(i,j-1,mat,dp)
        up = self.paths(i-1,j,mat,dp)
        dp[i][j] = up+left
        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if obstacleGrid else 0
        if obstacleGrid[0][0]==1:
            return 0
        prev = [0]*n

        for i in range(m):
            temp = [0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[0] = 1
                else:
                    if obstacleGrid[i][j]==1:
                        temp[j] = 0
                        continue
                    temp[j] = prev[j]+temp[j-1]
            prev = temp
        return prev[n-1]
        