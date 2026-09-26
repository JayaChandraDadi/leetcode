class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) if m else 0
        drc = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(r,c,board,visited,index):
            if index==len(word):
                return True
            visited[r][c] = 1
            for dr,dc in drc:
                nr = r + dr
                nc = c + dc
                if nr>=0 and nr<m and nc>=0 and nc<n and board[nr][nc]==word[index] and visited[nr][nc]==0:
                    if dfs(nr,nc,board,visited,index+1):
                        return True
            visited[r][c] = 0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited = [[0]*n for _ in range(m)]
                    if dfs(i,j,board,visited,1):
                        return True
        return False