from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue = deque()
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        drow = [-1, -1, 0, +1, +1, +1, 0, -1]
        dcol = [0, +1, +1, +1, 0, -1, -1, -1]
        queue.append([1,0,0])
        dist[0][0] = 0
        while(len(queue)!=0):
            distance,r,c = queue.popleft()
            if r==n-1 and c==n-1:
                return distance
            for i in range(8):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<n and dist[nrow][ncol]>distance+1 and grid[nrow][ncol]==0:
                    dist[nrow][ncol] = distance+1
                    queue.append([distance+1,nrow,ncol])
        return -1
