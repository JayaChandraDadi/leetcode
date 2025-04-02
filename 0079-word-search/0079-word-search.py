class Solution(object):
    def analyze(self,row,col,board,word,temp,i,n,vis,m):
        if word==temp:
            return True
        if row+1<m and board[row+1][col]==word[i] and vis[row+1][col]!=1:
            temp.append(board[row+1][col])
            vis[row+1][col] = 1
            if self.analyze(row+1,col,board,word,temp,i+1,n,vis,m):
                return True
            temp.pop()
            vis[row+1][col] = 0
        if col-1>=0 and board[row][col-1]==word[i] and vis[row][col-1]!=1:
            temp.append(board[row][col-1])
            vis[row][col-1] = 1
            if self.analyze(row,col-1,board,word,temp,i+1,n,vis,m):
                return True
            temp.pop()
            vis[row][col-1] = 0
        if col+1<n and board[row][col+1]==word[i] and vis[row][col+1]!=1:
            temp.append(board[row][col+1])
            vis[row][col+1] = 1
            if self.analyze(row,col+1,board,word,temp,i+1,n,vis,m):
                return True
            temp.pop()
            vis[row][col+1] = 0
        if row-1>=0 and board[row-1][col]==word[i] and vis[row-1][col]!=1:
            temp.append(board[row-1][col])
            vis[row-1][col] = 1
            if self.analyze(row-1,col,board,word,temp,i+1,n,vis,m):
                return True
            temp.pop()
            vis[row-1][col] = 0
        return False
        
    def exist(self, board, word):
        word = list(word)
        temp = []
        m = len(board)
        n = len(board[0])
        vis = [[0]*n for _ in range(m)]
        for col in range(n):
            for row in range(m):
                if board[row][col]==word[0]:
                    vis[row][col] = 1
                    temp.append(board[row][col])
                    if self.analyze(row,col,board,word,temp,1,n,vis,m):
                        return True
                    vis[row][col] = 0
                    temp.pop()
        return False

