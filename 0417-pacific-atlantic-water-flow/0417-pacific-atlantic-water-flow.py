class Solution:
    def dfs(self,grid,r,c,visited,drc,m,n):
        visited[r][c] = True
        for dr,dc in drc:
            nr = r + dr
            nc = c + dc
            if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]>=grid[r][c] and visited[nr][nc]==False:
                self.dfs(grid,nr,nc,visited,drc,m,n)
        return 
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0]) if m else 0
        pacific = [[False]*n for _ in range(m)]
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(m):
            self.dfs(heights,i,0,pacific,drc,m,n)
        for j in range(n):
            self.dfs(heights,0,j,pacific,drc,m,n)
        atlantic = [[False]*n for _ in range(m)]
        for i in range(m):
            self.dfs(heights,i,n-1,atlantic,drc,m,n)
        for j in range(n):
            self.dfs(heights,m-1,j,atlantic,drc,m,n)
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j]==True and atlantic[i][j]==True:
                    ans.append([i,j])
        return ans