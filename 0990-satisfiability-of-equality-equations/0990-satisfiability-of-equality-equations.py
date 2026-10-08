class Solution:
    def find(self,parent,x):
        if x!=parent[x]:
            parent[x] = self.find(parent,parent[x])
        return parent[x]
    def union(self,u,v,parent,size):
        pu = self.find(parent,u)
        pv = self.find(parent,v)
        if pv==pu:
            return 
        if size[pu]>size[pv]:
            parent[pv] = pu
            size[pu]+=size[pv]
        elif size[pv]>size[pu]:
            parent[pu] = pv
            size[pv]+=size[pu]
        else:
            parent[pv] = pu
            size[pu]+=size[pv]
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = {}
        size = {}
        for equation in equations:
            if equation[1]=='!':
                continue
            if equation[0] not in parent:
                parent[equation[0]] = equation[0]
                size[equation[0]] = 1
            if equation[3] not in parent:
                parent[equation[3]] = equation[3]
                size[equation[3]] = 1
            self.union(equation[0],equation[3],parent,size)
        for equation in equations:
            if equation[1]=='=':
                continue
            if equation[0] not in parent:
                parent[equation[0]] = equation[0]
                size[equation[0]] = 1
            if equation[3] not in parent:
                parent[equation[3]] = equation[3]
                size[equation[3]] = 1
            pu = self.find(parent,equation[0])
            pv = self.find(parent,equation[3])
            if pu==pv:
                return False
        return True