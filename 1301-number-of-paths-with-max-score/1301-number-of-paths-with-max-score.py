class Solution:
    def dfs(self,r,c,board,dp):
        if r<0 or c<0 or board[r][c]=='X':
            return [float('-inf'),0]
        if board[r][c]=='E':
            return [0,1]
        if dp[r][c]!=-1:
            return dp[r][c]
        up =   self.dfs(r-1,c,board,dp)
        left =  self.dfs(r,c-1,board,dp)
        diag = self.dfs(r-1,c-1,board,dp)
        maxsum = max(up[0],left[0],diag[0])
        if maxsum==float('-inf'):
            dp[r][c] = [float('-inf'),0]
            return dp[r][c]
        newct = 0
        if maxsum==up[0]:
            newct+=up[1]
        if maxsum==left[0]:
            newct+=left[1]
        if maxsum==diag[0]:
            newct+=diag[1]
        curr = 0
        if board[r][c].isdigit():
            curr = int(board[r][c])
            maxsum+=curr
        dp[r][c] = [maxsum,(newct)%(10**9 + 7)]
        return dp[r][c]
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        for i in range(m):
            s = list(board[i])
            board[i] = s
        n = len(board[0]) if m else 0
        dp = [[-1]*(n) for _ in range(m)]
        ans = self.dfs(m-1,n-1,board,dp)
        if ans[1]==0:
            return [0,0]
        return ans