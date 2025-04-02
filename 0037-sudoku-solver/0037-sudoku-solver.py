class Solution(object):
    def solveSudoku(self, board):
        # Create tracking sets for row, column, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []  # To store empty cell positions

        # Initialize sets and find empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def solve(index=0):
            if index == len(empty_cells):  # If all cells are filled, puzzle solved
                return True
            
            i, j = empty_cells[index]
            box_index = (i // 3) * 3 + (j // 3)

            for num in "123456789":
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_index]:
                    # Place the number
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)

                    if solve(index + 1):  # Recur for the next cell
                        return True
                    
                    # Backtrack
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)

            return False  # If no number fits, backtrack

        solve()

        
        