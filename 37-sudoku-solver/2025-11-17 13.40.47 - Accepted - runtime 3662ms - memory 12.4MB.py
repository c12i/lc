class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows, cols, boxes = [set() for _ in range(n)], [set() for _ in range(n)], [set() for _ in range(n)]
        empty_positions = []

        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    box_id = self.getBoxId(r, c)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)
                else:
                    empty_positions.append((r, c)) 

        self.solveRecursively(
            board,
            rows,
            cols,
            boxes,
            empty_positions, 
            0,
        )

    def solveRecursively(self, board, rows, cols, boxes, empty_positions, pos):
        if pos == len(empty_positions):
            return True # solved

        r, c = empty_positions[pos]
        box_id = self.getBoxId(r, c)
        
        for num in range(1, 9 + 1):
            if self.isValidSudoku(rows[r], cols[c], boxes[box_id], num):
                board[r][c] = str(num)
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

                if self.solveRecursively(board, rows, cols, boxes, empty_positions, pos + 1):
                    return True
                    
                # A call in the recursive stack yeileded false, which will only happen
                # when `isValidSudoku` is False. Because of this, backtrack
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_id].remove(num)

        return False


    def getBoxId(self, row, col):
        col = col // 3
        row = (row // 3) * 3
        return row + col

    
    def isValidSudoku(self, rows, cols, boxes, num):
        return (
            num not in rows and
            num not in cols and
            num not in boxes
        )