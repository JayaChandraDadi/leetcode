class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        weight = {}
        def find(x):
            if x!=parent[x]:
                old = parent[x]
                root = find(old)
                weight[x]*=weight[old]
                parent[x] = root
            return parent[x]
        def union(u,v,value):
            root_u = find(u)
            root_v = find(v)
            if root_u==root_v:
                return 
            parent[root_u] = root_v
            weight[root_u] = value*(weight[v]/weight[u])
        for i in range(len(equations)):
            u = equations[i][0]
            v = equations[i][1]
            if u not in parent:
                parent[u] = u
                weight[u] = 1
            if v not in parent:
                parent[v] = v
                weight[v] = 1
            union(u,v,values[i])
        ans = []
        for u,v in queries:
            if u not in parent or v not in parent:
                ans.append(-1)
                continue
            root_u = find(u)
            root_v = find(v)
            if root_u!=root_v:
                ans.append(-1)
            else:
                ans.append(weight[u]/weight[v])
        return ans