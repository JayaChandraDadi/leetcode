class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        dp = [[-1]*n for _ in range(m)]
        def dfs(i,j,grid):
            if i<0 or j<0 or grid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            left = 0 
            left+=dfs(i,j-1,grid)
            up = 0
            up+=dfs(i-1,j,grid)
            dp[i][j] = left + up
            return dp[i][j]
        return dfs(m-1,n-1,grid)