class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)

        sq_map = {}

        # check rows
        for i in range(n):
            digits = set()
            for j in range(n):
                val = board[i][j]

                if val == '.':
                    continue

                if val in digits:
                    return False

                digits.add(val)

        # check cols
        for i in range(n):
            digits = set()
            for j in range(n):
                val = board[j][i]

                if val == '.':
                    continue

                if val in digits:
                    return False

                digits.add(val)

        # build sq_map and check boxes
        for i in range(n):
            for j in range(n):
                val = board[i][j]

                if val == ".":
                    continue

                box_key = (i // 3, j // 3)

                if box_key not in sq_map:
                    sq_map[box_key] = set()

                if val in sq_map[box_key]:
                    return False
                else:
                    sq_map[box_key].add(val)
        
        return True
