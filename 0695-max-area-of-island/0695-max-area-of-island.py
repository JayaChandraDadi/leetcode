class Solution:
    def dfs(self,r,c,grid,m,n,drc,visited):
        visited[r][c] = True
        area = 1
        for dr,dc in drc:
            nr = r + dr
            nc = c + dc
            if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==False and grid[nr][nc]==1:
                area+=self.dfs(nr,nc,grid,m,n,drc,visited)
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        visited = [[False]*n for _ in range(m)]
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        maxarea = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==False:
                    area = 1
                    visited[i][j] = True
                    q.append((i,j))
                    while(q):
                        r,c = q.popleft()
                        for dr,dc in drc:
                            nr = r + dr
                            nc = c + dc
                            if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==False and grid[nr][nc]==1:
                                area+=1
                                q.append((nr,nc))
                                visited[nr][nc] = True
                    maxarea = max(maxarea,area)
        return maxarea