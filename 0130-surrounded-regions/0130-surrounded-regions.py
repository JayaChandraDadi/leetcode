from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0]) if m else 0
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        q = deque()
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            if board[i][0]=='O' and visited[i][0]==False:
                visited[i][0] = True
                q.append((i,0))
        for i in range(m):
            if board[i][n-1]=='O' and visited[i][n-1]==False:
                visited[i][n-1] = True
                q.append((i,n-1))
        for j in range(n):
            if board[0][j]=='O' and visited[0][j]==False:
                visited[0][j] = True
                q.append((0,j))
        for j in range(n):
            if board[m-1][j]=='O' and visited[m-1][j]==False:
                visited[m-1][j] = True
                q.append((m-1,j))
        while(q):
            r,c = q.popleft()
            for dr,dc in drc:
                nr = r + dr
                nc = c + dc
                if nr>=0 and nr<m and nc>=0 and nc<n and board[nr][nc]=='O' and visited[nr][nc]==False:
                    visited[nr][nc] = True
                    q.append((nr,nc))
        for i in range(m):
            for j in range(n):
                if visited[i][j]==False and board[i][j]=='O':
                    board[i][j] = 'X'