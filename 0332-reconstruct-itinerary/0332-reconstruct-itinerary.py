import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = set()
        adj = {}
        for dept,ari in tickets:
            if dept not in adj:
                adj[dept] = []
            heapq.heappush(adj[dept],(ari))
        ans = []
        def dfs(node):
            if not node:
                return 
            while node in adj and adj[node]:
                next_airport = heapq.heappop(adj[node])
                dfs(next_airport)
            ans.append(node)
        dfs('JFK')
        return ans[::-1]