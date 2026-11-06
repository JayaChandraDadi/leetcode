class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        boxmap = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in rowmap[i] or board[i][j] in colmap[j] or board[i][j] in boxmap[(i//3,j//3)]:
                    return False
                rowmap[i].add(board[i][j])
                colmap[j].add(board[i][j])
                boxmap[(i//3,j//3)].add(board[i][j])
        return True