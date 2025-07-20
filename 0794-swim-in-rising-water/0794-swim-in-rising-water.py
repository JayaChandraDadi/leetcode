import heapq
class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        vis = [[0]*n for _ in range(n)]
        pq = []
        heapq.heappush(pq,(grid[0][0],0,0))
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        while(pq):
            time,row,col = heapq.heappop(pq)
            if row==n-1 and col==n-1:
                return time
            vis[row][col] = 1
            for i in range(4):
                nrow = row+drow[i]
                ncol = col+dcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<n and vis[nrow][ncol]==0:
                    vis[nrow][ncol] = 1
                    heapq.heappush(pq,(max(time,grid[nrow][ncol]),nrow,ncol))
