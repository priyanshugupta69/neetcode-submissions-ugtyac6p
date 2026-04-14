from collections import defaultdict
class Solution:
    def check_rows(self, board):
        for i in range(len(board)):
            mp = defaultdict(bool)
            for j in range(len(board)):
                if board[i][j] != '.' and mp[board[i][j]] == True:
                    return False
                mp[board[i][j]] = True
        return True

    def check_cols(self, board):
        for i in range(len(board)):
            mp = defaultdict(bool)
            for j in range(len(board)):
                if board[j][i] != '.' and mp[board[j][i]] == True:
                    return False
                mp[board[j][i]] = True
        return True

    def check_grid(self, board):
        i = 0

        while(i < 9):
            j = 0
            while(j < 9):
                mp = defaultdict(bool)
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.' and mp[board[x][y]] == True:
                            return False
                        mp[board[x][y]] = True
                j += 3
            i += 3
        return True
                     

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board) and self.check_cols(board) and self.check_grid(board)
        