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
        up = 0
        left = 0
        prev = [0]*n
        for i in range(m):
            temp = [0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i>0:
                        up = grid[i][j]+prev[j]
                    else:
                        up = float('inf')
                    left= grid[i][j] 
                    if j>0:
                        left = grid[i][j] + temp[j-1]
                    else:
                        left = float('inf')
                    temp[j] = min(up,left)
            prev = temp
        return prev[n-1]
        