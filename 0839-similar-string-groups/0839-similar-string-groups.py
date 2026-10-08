class Solution:
    def similar(self,s1,s2):
        changes = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                changes+=1
            if changes>2:
                return False
        if changes<=2:
            return True
        return False
    def find(self,x,parent):
        if x!=parent[x]:
            parent[x] = self.find(parent[x],parent)
        return parent[x]
    def union(self,u,v,size,parent):
        pu = self.find(u,parent)
        pv = self.find(v,parent)
        if size[pu]>size[pv]:
            size[pu]+=size[pv]
            parent[pv] = pu
        elif size[pv]>size[pu]:
            size[pv]+=size[pu]
            parent[pu] = pv
        else:
            size[pv]+=size[pu]
            parent[pu] = pv
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        edges = []
        size = {}
        parent = {}
        components = 0
        for i in range(n):
            parent[strs[i]] = strs[i]
            size[strs[i]] = 1
            for j in range(i+1,n):
                if self.similar(strs[i],strs[j]):
                    edges.append([strs[i],strs[j]])
        for u,v in edges:
            self.union(u,v,size,parent)
        for x,parx in parent.items():
            if x==parx:
                components+=1
        return components