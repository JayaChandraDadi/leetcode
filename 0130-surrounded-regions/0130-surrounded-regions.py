class Solution(object):
    def dfs(self,vis,board,drow,dcol,r,c,m,n):
        vis[r][c] = 1
        for i in range(4):
            nrow = r + drow[i]
            ncol = c + dcol[i]
            if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]==0 and board[nrow][ncol]=='O':
                self.dfs(vis,board,drow,dcol,nrow,ncol,m,n)

    def solve(self, board):
        m = len(board)
        n = len(board[0]) if board else 0
        vis = []
        drow = [-1,0,+1,0]
        dcol = [0,+1,0,-1]
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            vis.append(temp)
        for i in range(m):
            if not vis[i][0] and board[i][0]=='O':
                self.dfs(vis,board,drow,dcol,i,0,m,n)
            if not vis[i][n-1] and board[i][n-1]=='O':
                self.dfs(vis,board,drow,dcol,i,n-1,m,n)
        for i in range(1,n-1):
            if not vis[0][i] and board[0][i]=='O':
                self.dfs(vis,board,drow,dcol,0,i,m,n)
            if not vis[m-1][i] and board[m-1][i]=='O':
                self.dfs(vis,board,drow,dcol,m-1,i,m,n)
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and board[i][j]=='O':
                    board[i][j]='X'
        


        
        