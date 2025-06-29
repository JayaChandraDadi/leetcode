from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0]) if grid else 0
        queue = deque()
        vis = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])  
                    vis[i][j] = 2
                elif grid[i][j] == 1:
                    vis[i][j] = 1
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        mintime = 0
        while(len(queue)!=0):
            node = queue.popleft()
            r = node[0]
            c = node[1]
            time = node[2]
            mintime = max(mintime,time)
            for i in range(4):
                nrow = r+drow[i]
                ncol = c+dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]!=2 and grid[nrow][ncol]==1:
                    queue.append([nrow,ncol,time+1])
                    vis[nrow][ncol] = 2
        for i in range(m):
            for j in range(n):
                if vis[i][j]==1 and vis[i][j]!=2:
                    return -1
        return mintime
