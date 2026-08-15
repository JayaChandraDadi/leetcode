class Solution:
    def dfs(self,grid,r,c,m,n,distance,drc):
        grid[r][c] = distance
        for dr,dc in drc:
            nr = r + dr
            nc = c + dc
            if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]!=-1:
                if grid[nr][nc]>distance + 1:
                    self.dfs(grid,nr,nc,m,n,distance+1,drc)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0]) if m else 0
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    self.dfs(rooms,i,j,m,n,0,drc)
