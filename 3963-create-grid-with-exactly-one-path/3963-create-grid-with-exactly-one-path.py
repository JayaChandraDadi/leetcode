class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        mat = [['#']*n for _ in range(m)]
        for i in range(m):
            mat[i][0] = '.'
        for j in range(n):
            mat[m-1][j] = '.'
        ans = []
        for i in range(m):
            ans.append(''.join(mat[i]))
        return ans