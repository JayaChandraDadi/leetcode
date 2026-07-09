class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row_map[i] or board[i][j] in col_map[j] or board[i][j] in box_map[(i//3,j//3)]:
                    return False
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                box_map[(i//3,j//3)].add(board[i][j])
        return True
