class Solution(object):
    def findboard(self,board,row,col,i,vis,m,n,word):
        if i==len(word):
            return True
        if row+1<m:
            if word[i]==board[row+1][col] and vis[row+1][col]==0:
                vis[row+1][col] = 1
                if self.findboard(board,row+1,col,i+1,vis,m,n,word):
                    return True
                vis[row+1][col] = 0
        if col+1<n:
            if word[i]==board[row][col+1] and vis[row][col+1]==0:
                vis[row][col+1] = 1
                if self.findboard(board,row,col+1,i+1,vis,m,n,word):
                    return True
                vis[row][col+1] = 0
        if row-1>=0:
            if word[i]==board[row-1][col] and vis[row-1][col]==0:
                vis[row-1][col] = 1
                if self.findboard(board,row-1,col,i+1,vis,m,n,word):
                    return True
                vis[row-1][col] = 0
        if col-1>=0:
            if word[i]==board[row][col-1] and vis[row][col-1]==0:
                vis[row][col-1] = 1
                if self.findboard(board,row,col-1,i+1,vis,m,n,word):
                    return True
                vis[row][col-1] = 0
        return False
    def exist(self, board, word):
        m = len(board)
        n = len(board[0]) if m else 0
        vis = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    vis[i][j] = 1
                    if self.findboard(board,i,j,1,vis,m,n,word):
                        return True
                    vis[i][j] = 0
        return False
        