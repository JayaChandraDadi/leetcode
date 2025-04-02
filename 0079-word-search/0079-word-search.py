class Solution(object):
    def analyze(self,row,col,board,word,i,n,vis,m):
        if i==len(word):
            return True
        if row+1<m and board[row+1][col]==word[i] and vis[row+1][col]!=1:
            vis[row+1][col] = 1
            if self.analyze(row+1,col,board,word,i+1,n,vis,m):
                return True
            vis[row+1][col] = 0
        if col-1>=0 and board[row][col-1]==word[i] and vis[row][col-1]!=1:
            vis[row][col-1] = 1
            if self.analyze(row,col-1,board,word,i+1,n,vis,m):
                return True
            vis[row][col-1] = 0
        if col+1<n and board[row][col+1]==word[i] and vis[row][col+1]!=1:
            vis[row][col+1] = 1
            if self.analyze(row,col+1,board,word,i+1,n,vis,m):
                return True
            vis[row][col+1] = 0
        if row-1>=0 and board[row-1][col]==word[i] and vis[row-1][col]!=1:
            vis[row-1][col] = 1
            if self.analyze(row-1,col,board,word,i+1,n,vis,m):
                return True
            vis[row-1][col] = 0
        return False
        
    def exist(self, board, word):
        word = list(word)
        m = len(board)
        n = len(board[0])
        vis = [[0]*n for _ in range(m)]
        for col in range(n):
            for row in range(m):
                if board[row][col]==word[0]:
                    vis[row][col] = 1
                    if self.analyze(row,col,board,word,1,n,vis,m):
                        return True
                    vis[row][col] = 0
        return False

