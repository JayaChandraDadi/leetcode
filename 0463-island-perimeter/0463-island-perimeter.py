from collections import deque
class Solution:
    def dfs(self,r,c,visited,drc,grid,m,n):
        visited[r][c] = True
        perimeter = 0
        for dr,dc in drc:
            nr = r + dr
            nc = c + dc
            if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==False and grid[nr][nc]==1:
                perimeter+=self.dfs(nr,nc,visited,drc,grid,m,n)
            elif nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1 and visited[nr][nc]==True:
                continue
            else:
                perimeter+=1
        return perimeter
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        q = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    visited = [[False]*n for _ in range(m)]
                    drc = [(-1,0),(0,1),(1,0),(0,-1)]
                    q.append((i,j))
                    visited[i][j] = True
                    while(q):
                        r,c = q.popleft()
                        perimeter = 0
                        for dr,dc in drc:
                            nr = r + dr
                            nc = c + dc
                            if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==False and grid[nr][nc]==1:
                                q.append((nr,nc))
                                visited[nr][nc] = True
                            elif nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1 and visited[nr][nc]==True:
                                continue
                            else:
                                perimeter+=1
                        ans+=perimeter
                    return ans