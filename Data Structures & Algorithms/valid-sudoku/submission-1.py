class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for i in range(9)]
        column = [[] for i in range(9)]
        square = [[] for i in range(9)]
        size = len(board)
        for i in range(size):
            for j in range(size):
                if(board[i][j].isdigit()):
                    if(board[i][j] not in row[i]):
                        row[i].append(board[i][j])
                    else:
                        return False
                    if(board[i][j] not in column[j]):
                        column[j].append(board[i][j])
                    else:
                        return False
                    square_val = math.floor(i/3) * 3 + math.floor(j/3)
                    if(board[i][j] not in square[square_val]):
                        square[square_val].append(board[i][j])
                    else:
                        return False
        return True