from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        ans = []
        for i in range(len(values)):
            u = equations[i][0]
            v = equations[i][1]
            weight = values[i]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append([v,weight])
            graph[v].append([u,1/weight])
        for start,end in queries:
            if start not in graph or end not in graph:
                ans.append(-1)
                continue
            q = deque()
            q.append((start,1.0))
            visited = set()
            visited.add((start))
            flag = -1
            while(q):
                node,weight = q.popleft()
                if node==end:
                    ans.append(weight)
                    flag = 0
                    break
                for nei,fraction in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,fraction*weight))
            if flag==-1:
                ans.append(-1)
        return ans
            