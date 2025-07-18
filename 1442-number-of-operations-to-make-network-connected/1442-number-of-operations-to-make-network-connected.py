class Solution(object):
    def findpar(self,node,parent):
        if parent[node]==node:
            return node
        parent[node] = self.findpar(parent[node],parent)
        return parent[node]
    def unionbyrank(self,u,v,rank,parent):
        pu = self.findpar(u,parent)
        pv = self.findpar(v,parent)
        if rank[pu]<rank[pv]:
            parent[pu] = pv
        elif rank[pv]<rank[pu]:
            parent[pv] = pu
        else:
            parent[pu] = pv
            rank[pv]+=1
    def makeConnected(self, n, connections):
        parent = [0]*n
        for i in range(n):
            parent[i] = i
        rank = [0]*n
        extras = 0
        nc = 0
        for it in connections:
            u = it[0]
            v = it[1]
            if self.findpar(u,parent)!=self.findpar(v,parent):
                self.unionbyrank(u,v,rank,parent)
            else:
                extras+=1
        for i in range(n):
            if parent[i]==i:
                nc+=1
        if extras>=nc-1:
            return (nc-1)
        else:
            return -1