import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0]) if m else 0
        if m==1 and n==1:
            return 0
        dist = [[float('inf')]*n for _ in range(m)]
        pq = []
        heapq.heappush(pq,(0,0,float('-inf')))
        drc = [[-1,0],[0,1],[1,0],[0,-1]]
        while(pq):
            r,c,min_effort = heapq.heappop(pq)
            if r==m-1 and c==n-1:
                return min_effort
            for dr,dc in drc:
                nr = r + dr
                nc = c + dc
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    effort = max(abs(heights[nr][nc] - heights[r][c]),min_effort)
                    if effort<dist[nr][nc]:
                        dist[nr][nc] = effort
                        heapq.heappush(pq,(nr,nc,effort))
        return 0