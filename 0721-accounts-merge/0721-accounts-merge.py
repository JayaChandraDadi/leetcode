class Solution:
    def findpar(self,x,parent):
        if x!=parent[x]:
            parent[x] = self.findpar(parent[x],parent)
        return parent[x]
    def union(self,u,v,parent,size):
        pu = self.findpar(u,parent)
        pv = self.findpar(v,parent)
        if pu==pv:
            return 
        if size[pu]<size[pv]:
            size[pv]+=size[pu]
            parent[pu] = pv
        elif size[pv]<size[pu]:
            size[pu]+=size[pv]
            parent[pv] = pu
        else:
            size[pu]+=size[pv]
            parent[pv] = pu
        return 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = {}
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                parent[email] = email
                size[email] = 1
        for account in accounts:
            name = account[0]
            email1 = account[1]
            for email2 in account[2:]:
                self.union(email1,email2,parent,size)
        components = {}
        for email in parent:
            root = self.findpar(email,parent)
            if root not in components:
                components[root] = []
            components[root].append(email)
        ans = []
        for root in components:
            name = email_to_name[root]
            emails = sorted(components[root])
            ans.append([name] + emails)
        return ans