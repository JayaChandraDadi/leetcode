from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        vis =[[]]
        m = len(image)
        n = len(image[0]) if image else 0
        vis = image
        queue = deque()
        prevcolor = image[sr][sc]
        vis[sr][sc] = 1
        image[sr][sc] = color
        queue.append([sr,sc])
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        while(len(queue)!=0):
            r,c = queue.popleft()
            for i in range(4):
                nrow = r+drow[i]
                ncol = c+dcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and image[nrow][ncol]==prevcolor and vis[nrow][ncol]!=color:
                    vis[nrow][ncol] = 1
                    image[nrow][ncol] = color
                    queue.append([nrow,ncol])
        return image


        
        