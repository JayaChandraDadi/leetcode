class Solution:
    def dfs(self,r,c,grid,visited,m,n,drc):
        visited[r][c] = True
        for dr,dc in drc:
            nr = r + dr
            nc = c + dc
            if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==False and grid[nr][nc]=='1':
                self.dfs(nr,nc,grid,visited,m,n,drc)
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        visited = [[False]*n for _ in range(m)]
        ct = 0
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==False:
                    ct+=1
                    self.dfs(i,j,grid,visited,m,n,drc)
        return ct