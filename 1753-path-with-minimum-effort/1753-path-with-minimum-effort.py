import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        pq = []
        heapq.heappush(pq,(0,0,0))
        m = len(heights)
        n = len(heights[0]) if heights else 0
        dist = [[float('inf')] * n for _ in range(m)]
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        while(pq):
            diff,r,c = heapq.heappop(pq)
            if r==m-1 and c==n-1:
                return diff
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n:
                    neweffort = max(abs(heights[nrow][ncol]-heights[r][c]),diff)
                    if neweffort<dist[nrow][ncol]:
                        dist[nrow][ncol] = neweffort
                        heapq.heappush(pq,(neweffort,nrow,ncol))
        