class Solution(object):
    def solve(self,n,board,col,leftrow,lowerdiagonal,upperdiagonal,res):
        if col==n:
            res.append(["".join(row) for row in board])  
            return
        for row in range(n):
            if leftrow[row]==0 and lowerdiagonal[row+col]==0 and upperdiagonal[n-1+col-row]==0:
                board[row][col] = "Q"
                leftrow[row] = 1
                lowerdiagonal[row+col] = 1
                upperdiagonal[n-1+col-row] = 1
                self.solve(n,board,col+1,leftrow,lowerdiagonal,upperdiagonal,res)
                board[row][col] ="."
                leftrow[row] = 0
                lowerdiagonal[row+col] = 0
                upperdiagonal[n-1+col-row] = 0
    def solveNQueens(self, n):
        res = []
        board = [["." for _ in range(n)] for _ in range(n)] 
        leftrow = [0]*n
        lowerdiagonal = [0]*((2*n)-1)
        upperdiagonal = [0]*((2*n)-1)
        self.solve(n,board,0,leftrow,lowerdiagonal,upperdiagonal,res)
        return res
        