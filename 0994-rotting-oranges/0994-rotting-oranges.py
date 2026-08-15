from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        q = deque()
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
        minutes = 0
        while(q):
            k = len(q)
            for i in range(k):
                r,c = q.popleft()
                for dr,dc in drc:
                    nr = r + dr
                    nc = c + dc
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            if q:
                minutes+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return minutes