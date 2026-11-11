from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        visited = [[False]*n for _ in range(m)]
        drc = [(0,-1),(-1,0),(1,0),(0,1)]
        ans = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0 and visited[i][j]==False:
                    q = deque()
                    q.append((i,j))
                    flag = 1
                    visited[i][j] = True
                    while(q):
                        r,c = q.popleft()
                        for dr,dc in drc:
                            nr = r + dr
                            nc = c + dc
                            if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==False and grid[nr][nc]==0:
                                if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                                    flag = 0
                                q.append((nr,nc))
                                visited[nr][nc] = True
                    if flag==1:
                        ans+=1
        return ans
