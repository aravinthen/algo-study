class Solution:
    def valid_row(self, board, row_ind):
        count = {str(i): 0 for i in range(1, 10)}
        for val in board[row_ind]:
            if val == ".":
                continue

            count[val] += 1
            if count[val] > 1:
                return False

        return True

    def valid_col(self, board, col_ind):
        # obtain the column first
        col = [i[col_ind] for i in board]
        count = {str(i): 0 for i in range(1, 10)}
        for val in col:
            if val == ".":
                continue

            count[val] += 1
            if count[val] > 1:
                return False

        return True

    def valid_square(self, board, square_ind):
        # square_ind [0-3], [0-3]
        # obtain the square
        square = []

        # very lazy solution
        mapping = {
            0: (0, 0),
            1: (3, 0),
            2: (6, 0),
            3: (0, 3),
            4: (3, 3),
            5: (6, 3),
            6: (0, 6),
            7: (3, 6),
            8: (6, 6),
        }

        conv_s = mapping[square_ind]

        row_start, row_end = conv_s[0], conv_s[0] + 3
        col_start, col_end = conv_s[1], conv_s[1] + 3

        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                square.append(board[i][j])

        count = {str(i): 0 for i in range(1, 10)}
        for val in square:
            if val == ".":
                continue
                
            count[val] += 1 
            if count[val] > 1:
                return False


        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for index in range(0, 9):
            if not self.valid_row(board, index):
                return False
            if not self.valid_col(board, index):
                return False
            if not self.valid_square(board, index):
                return False

        return True
