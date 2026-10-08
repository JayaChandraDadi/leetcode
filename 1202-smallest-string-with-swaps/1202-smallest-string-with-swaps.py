class Solution:
    def find(self,x,parent):
        if x!=parent[x]:
            parent[x] = self.find(parent[x],parent)
        return parent[x]
    def union(self,u,v,parent,size):
        pu = self.find(u,parent)
        pv = self.find(v,parent)
        if pu==pv:
            return
        if size[pu]>size[pv]:
            size[pu]+=size[pv]
            parent[pv] = pu
        elif size[pv]>size[pu]:
            size[pv]+=size[pv]
            parent[pu] = pv
        else:
            size[pu]+=size[pv]
            parent[pv] = pu
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        hashmap = {}
        for i in range(len(s)):
            hashmap[i] = s[i]
        ans = [0]*len(s)
        parent = [i for i in range(len(s))]
        size = [1]*len(s)
        for u,v in pairs:
            self.union(u,v,parent,size)
        root_to_component = {}
        for i in range(len(parent)):
            root = self.find(i,parent)
            if root not in root_to_component:
                root_to_component[root] = []
            root_to_component[root].append(i)
        for root,arr in root_to_component.items():
            characters = []
            for i in arr:
                characters.append(s[i])
            characters.sort()
            arr.sort()
            for i in range(len(arr)):
                index = arr[i]
                ch = characters[i]
                ans[index] = ch
        return ''.join(ans)