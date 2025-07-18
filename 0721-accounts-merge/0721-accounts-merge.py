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
    def accountsMerge(self, accounts):
        n = len(accounts)
        parent = [0]*n
        rank = [0]*n
        for i in range(n):
            parent[i] = i
        mapmailnode = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapmailnode:
                    mapmailnode[mail] = i
                else:
                    self.unionbyrank(i,mapmailnode[mail],rank,parent)
        mergedmail = [[]for _ in range(n)]
        for mail,index in mapmailnode.items():
            node = self.findpar(index,parent)
            mergedmail[node].append(mail)
        ans = []
        for i in range(n):
            if len(mergedmail[i])==0:
                continue
            mergedmail[i].sort()
            temp = []
            temp.append(accounts[i][0])
            for it in mergedmail[i]:
                temp.append(it)
            ans.append(temp)
        return ans

        
        