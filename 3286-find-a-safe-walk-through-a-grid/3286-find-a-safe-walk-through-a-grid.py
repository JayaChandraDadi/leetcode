from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0]) if m>0 else 0
        dist = [[float('inf')]*n for _ in range(m)]
        q = deque()
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        dist[0][0] = grid[0][0]
        q.append((0,0))
        while(q):
            r,c = q.popleft()
            for dr,dc in drc:
                nr = r + dr
                nc = c + dc
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    cost = grid[nr][nc]
                    damage = dist[r][c] + cost
                    if dist[nr][nc]>damage:
                        dist[nr][nc] = damage
                        if cost==0:
                            q.appendleft((nr,nc))
                        else:
                            q.append((nr,nc))
        if dist[m-1][n-1] < health:
            return True
        return False