from collections import deque
class Solution(object):
    def numIslands(self, grid):
        queue = deque()
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        m = len(grid)
        n = len(grid[0]) if grid else 0
        ct = 0
        vis = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and grid[i][j]=='1':
                    queue.append([i,j])
                    ct+=1
                    while(len(queue)!=0):
                        r,c = queue.popleft()
                        for k in range(4):
                            nrow = r + drow[k]
                            ncol = c + dcol[k]
                            if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]==0 and grid[nrow][ncol]=='1':
                                queue.append([nrow,ncol])
                                vis[nrow][ncol] = 1
        return ct


        