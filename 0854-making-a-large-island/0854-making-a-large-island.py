class Solution(object):
    def findpar(self,node,parent):
        if parent[node]==node:
            return node
        parent[node] = self.findpar(parent[node],parent)
        return parent[node]
    def unionbysize(self,u,v,size,parent):
        pu = self.findpar(u,parent)
        pv = self.findpar(v,parent)
        if size[pu]<size[pv]:
            parent[pu] = pv
            size[pv]+=size[pu]
        elif size[pv]<size[pu]:
            parent[pv] = pu
            size[pu]+=size[pv]
        else:
            parent[pu] = pv
            size[pv]+=size[pu]
    def largestIsland(self, grid):
        n = len(grid)
        parent = [0]*(n*n)
        size = [0]*(n*n)
        for i in range(n*n):
            parent[i] = i
        for i in range(n*n):
            size[i] = 1
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        for row in range(n):
            for col in range(n):
                if grid[row][col]==0:
                    continue
                rownode = (row*n)+col
                for i in range(4):
                    nrow = row+drow[i]
                    ncol = col+dcol[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                        if self.findpar((nrow*n)+ncol,parent)!=self.findpar((row*n)+col,parent):

                            adjrownode = (nrow*n)+ncol
                            self.unionbysize(rownode,adjrownode,size,parent)
        maxsize = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col]==1:
                    continue
                islandsize = 0
                rownode = (row*n)+col
                components = set()
                for i in range(4):
                    nrow = row+drow[i]
                    ncol = col+dcol[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                        components.add(self.findpar((nrow*n)+ncol,parent))
                for it in components:
                    islandsize+=size[it]
                maxsize = max(maxsize,islandsize+1)
        for node in range(n*n):
            maxsize = max(maxsize,size[self.findpar(node,parent)])
        return maxsize

          


        
        