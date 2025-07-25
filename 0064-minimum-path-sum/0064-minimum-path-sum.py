class Solution(object):
    def path(self,i,j,grid,dp):
        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=0:
            return dp[i][j]
        left = grid[i][j] + self.path(i,j-1,grid,dp)
        up = grid[i][j] + self.path(i-1,j,grid,dp)
        dp[i][j] = min(left,up)
        return dp[i][j]
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0]) if grid else 0
        dp = [[0]*n for i in range(m)]
        return self.path(m-1,n-1,grid,dp)
        