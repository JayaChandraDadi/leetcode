from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        vis =[[]]
        m = len(image)
        n = len(image[0]) if image else 0
        vis = [[0] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if i==sr and j==sc:
                    prevcolor = image[i][j]
                    vis[i][j] = 1
                    image[i][j] = color
                    queue.append([i,j])
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        while(len(queue)!=0):
            r,c = queue.popleft()
            for i in range(4):
                nrow = r+drow[i]
                ncol = c+dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and image[nrow][ncol]==prevcolor and vis[nrow][ncol]!=1:
                    vis[nrow][ncol] = 1
                    image[nrow][ncol] = color
                    queue.append([nrow,ncol])
        return image


        
        