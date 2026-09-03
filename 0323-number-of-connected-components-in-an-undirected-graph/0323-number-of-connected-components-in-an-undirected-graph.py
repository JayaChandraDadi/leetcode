class Solution:
    def findpar(self,x,parent):
        if parent[x]!=x:
            parent[x] = self.findpar(parent[x],parent)
        return parent[x]
    def union(self,u,v,parent,size):
        pu = self.findpar(u,parent)
        pv = self.findpar(v,parent)
        if size[pu]<size[pv]:
            size[pv]+=size[pu]
            parent[pu] = pv
        elif size[pv]<size[pu]:
            size[pu]+=size[pv]
            parent[pv]=pu
        else:
            size[pu]+=size[pv]
            parent[pv] = pu
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [0]*n
        ct = 0
        for i in range(n):
            parent[i] = i
        size = [1]*n
        for u,v in edges:
            self.union(u,v,parent,size)
        for i in range(n):
            if parent[i]==i:
                ct+=1
        return ct
