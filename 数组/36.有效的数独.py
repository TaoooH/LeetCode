# 暴力循环
# 行和列可以在同一个for中
# 单独对方块进行循环判定
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row, cloum = [], []
            for j in range(9):
                # 对每行进行判定
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.append(board[i][j])
                
                # 对每列进行判定
                if board[j][i] != '.':
                    if board[j][i] in cloum:
                        return False
                    else:
                        cloum.append(board[j][i])
        # 对每个九宫格进行判定
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sq = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] == '.':
                            continue
                        else:
                            if board[i + x][j + y] in sq:
                                return False
                            else:
                                sq.append(board[i + x][j + y])
        return True
