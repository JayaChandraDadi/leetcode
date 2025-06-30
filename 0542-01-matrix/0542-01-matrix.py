from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        queue = deque()
        m = len(mat)
        n = len(mat[0] if mat else 0)
        dist = mat
        vis = []
        for i in range(m):
            temp = []
            for j in range(n):
                if mat[i][j]==0:
                    queue.append([i,j,0])
                    temp.append(1)
                else:
                    temp.append(0)
            vis.append(temp)
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        while(len(queue)!=0):
            r,c,step = queue.popleft()
            dist[r][c] = step
            for i in range(4):
                nrow = r+drow[i]
                ncol = c+dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and mat[nrow][ncol]==1 and vis[nrow][ncol]==0:
                    queue.append([nrow,ncol,step+1])
                    vis[nrow][ncol] = 1
        return dist

        
        