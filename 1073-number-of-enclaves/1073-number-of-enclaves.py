class Solution(object):
    def dfs(self,grid,vis,r,c,m,n,drow,dcol):
        vis[r][c]=1
        for i in range(4):
            nrow = r+drow[i]
            ncol = c+dcol[i]
            if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]==0 and grid[nrow][ncol]==1:
                self.dfs(grid,vis,nrow,ncol,m,n,drow,dcol)

    def numEnclaves(self, grid):
        ct = 0
        m = len(grid)
        n = len(grid[0]) if grid else 0
        vis = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            vis.append(temp)
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        for i in range(m):
            if not vis[i][0] and grid[i][0]==1:
                self.dfs(grid,vis,i,0,m,n,drow,dcol)
            if not vis[i][n-1] and grid[i][n-1]==1:
                self.dfs(grid,vis,i,n-1,m,n,drow,dcol)
        for i in range(1,n-1):
            if not vis[0][i] and grid[0][i]==1:
                self.dfs(grid,vis,0,i,m,n,drow,dcol)
            if not vis[m-1][i] and grid[m-1][i]==1:
                self.dfs(grid,vis,m-1,i,m,n,drow,dcol)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]==0:
                    ct+=1
        return ct


        