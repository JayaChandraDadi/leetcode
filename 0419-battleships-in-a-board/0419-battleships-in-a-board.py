from collections import deque
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m = len(board)
        n = len(board[0]) if m else 0
        ct = 0
        drc = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X' and visited[i][j]==False:
                    q = deque()
                    q.append((i,j))
                    visited[i][j] = True
                    while(q):
                        r,c = q.popleft()
                        for dr,dc in drc:
                            nr = r + dr
                            nc = c + dc
                            if nr>=0 and nc>=0 and nr<m and nc<n and visited[nr][nc]==False and board[nr][nc]=='X':
                                visited[nr][nc] = True
                                q.append((nr,nc))
                    ct+=1
        return ct
                                
