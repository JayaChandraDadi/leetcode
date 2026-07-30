import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[profits[i],capital[i]] for i in range(len(profits))]
        projects.sort(key=lambda x:x[1])
        i = 0
        pq = []
        for _ in range(k):
            while i<len(projects) and projects[i][1]<=w:
                heapq.heappush(pq,(-projects[i][0]))
                i+=1
            if not pq:
                break
            w-=heapq.heappop(pq)
        return w