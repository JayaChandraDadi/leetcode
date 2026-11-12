from collections import deque
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        q = deque()
        n = len(grid[0]) if m else 0
        ans = 0
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==False:
                    visited[i][j] = True
                    q = deque()
                    q.append((i,j))
                    ct = 1
                    while(q):
                        r,c = q.popleft()
                        for nr in range(m):
                            if grid[nr][c]==1 and visited[nr][c]==False and nr!=r:
                                visited[nr][c] = True
                                q.append((nr,c))
                                ct+=1
                        for nc in range(n):
                            if grid[r][nc]==1 and visited[r][nc]==False and nc!=c:
                                visited[r][nc] = True
                                q.append((r,nc))
                                ct+=1
                    if ct>1:
                        ans+=ct
        return ans