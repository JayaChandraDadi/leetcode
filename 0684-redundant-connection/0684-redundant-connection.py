class Solution:
    def findpar(self,x,parent):
        if x!=parent[x]:
            parent[x] = self.findpar(parent[x],parent)
        return parent[x]
    def union(self,u,v,parent,size):
        pu = self.findpar(u,parent)
        pv = self.findpar(v,parent)
        if pu==pv:
            return False
        if size[pu]<size[pv]:
            size[pv]+=size[pu]
            parent[pu] = pv
        elif size[pv]<size[pu]:
            size[pu]+=size[pv]
            parent[pv] = pu
        else:
            size[pu]+=size[pv]
            parent[pv] = pu
        return True
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0]*(n+1)
        for i in range(n+1):
            parent[i] = i
        size = [1]*(n+1)
        for u,v in edges:
            if self.union(u,v,parent,size)==False:
                return [u,v]