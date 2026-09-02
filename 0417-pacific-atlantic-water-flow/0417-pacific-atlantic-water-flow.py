class Solution:
    def dfs(self,r,c,visited,heights,drc,m,n):
        visited[r][c] = True
        for dr,dc in drc:
            nr = r + dr
            nc = c + dc
            if nr>=0 and nr<m and nc>=0 and nc<n and heights[nr][nc]>=heights[r][c] and visited[nr][nc]==False:
                self.dfs(nr,nc,visited,heights,drc,m,n)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0]) if m else 0
        pacific_visited = [[False]*n for _ in range(m)]
        atlantic_visited = [[False]*n for _ in range(m)]
        ans = []
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(m):
            self.dfs(i,0,pacific_visited,heights,drc,m,n)
        for j in range(n):
            self.dfs(0,j,pacific_visited,heights,drc,m,n)
        for i in range(m):
            self.dfs(i,n-1,atlantic_visited,heights,drc,m,n)
        for j in range(n):
            self.dfs(m-1,j,atlantic_visited,heights,drc,m,n)
        for i in range(m):
            for j in range(n):
                if atlantic_visited[i][j]==True and pacific_visited[i][j]==True:
                    ans.append([i,j])
        return ans