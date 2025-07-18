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
    def removeStones(self, stones):
        maxrow = -1
        maxcol = -1
        ct = 0
        n = len(stones)
        for it in stones:
            maxrow = max(maxrow,it[0])
            maxcol = max(maxcol,it[1])
        parent = [0]*(maxrow+maxcol+2)
        rank = [0]*(maxrow+maxcol+2)
        mapp = set()
        for i in range(maxrow+maxcol+2):
            parent[i] = i
        for it in stones:
            rownode = it[0]
            colnode = it[1]+maxrow+1
            self.unionbyrank(rownode,colnode,rank,parent)
            mapp.add(rownode)
            mapp.add(colnode)
        for it in mapp:
            if self.findpar(it,parent)==it:
                ct+=1
        return n-ct
        