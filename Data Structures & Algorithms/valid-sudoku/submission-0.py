class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for i in board:
            maps = {}
            for j in i:
                if j in maps and j!=".":
                    valid = False
                maps[j] = 1
        for i in range(9):
            maps = {}
            for j in range(9):
                if board[j][i] in maps and board[j][i]!=".":
                    valid = False
                maps[board[j][i]] = 1
        for i in range(0,9,3):
            for j in range(0,9,3):
                maps = {}
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if board[row][col] in maps and board[row][col]!='.':
                            valid=False  
                        else:
                            maps[board[row][col]]=1
        return valid


