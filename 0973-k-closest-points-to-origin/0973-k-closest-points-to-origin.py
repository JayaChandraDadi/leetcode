import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x**2 + y**2
            heapq.heappush(pq,(dist,[x,y]))
        ans = []
        for i in range(k):
            dist,point = heapq.heappop(pq)
            ans.append(point)
        return ans