# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    编写一个程序，通过填充空格来解决数独问题。

    数独的解法需 遵循如下规则：

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
    数独部分空格内已填入了数字，空白格用 '.'表示。

    """
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        思路: 构造访问数组, 记录每个位置对应数字得可填性, 然后以人的思路先找那些快填满得空格子进行填充, 从而减少一层分支得遍历节点数
        """
        row = [[True] * 10 for _ in range(9)]
        col = [[True] * 10 for _ in range(9)]
        box = [[True] * 10 for _ in range(9)]

        def boxIndex(i, j):
            k = (i // 3) * 3 + j // 3
            return k

        # 初始化访问数组, 给每行每列每个格子已填过得数字位置设为 False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                digit = int(board[i][j])
                row[i][digit] = False
                col[j][digit] = False
                box[boxIndex(i, j)][digit] = False
        
        def findMinimumProbility(board):
            """
            找出最小分支数得格子, 返回其坐标, 通过计算每个格子的可能分支数, 找出最小可能分支的格子
            """
            minValue = 10
            pos = [-1, -1]
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    avaliableDigits = getAvaliableDigits(i, j)
                    if len(avaliableDigits) < minValue:
                        minValue = len(avaliableDigits)
                        pos = [i, j]
            return pos

        def getAvaliableDigits(i: int, j: int):
            """
            找出当前 (i, j) 索引下能填得全部可能数字
            """
            availableDigits = []
            for digit in range(1, 10):
                if row[i][digit] and col[j][digit] and box[boxIndex(i, j)][digit]:
                    availableDigits.append(digit)
            return availableDigits

        def dfs(board: List[List[str]]):
            pos = findMinimumProbility(board)
            x, y = pos
            if x == -1:
                return True
            
            availableDigits = getAvaliableDigits(x, y)
            for digit in availableDigits:
                # 填了对应的格子, 就记录对应的数字已经填过
                board[x][y] = str(digit)
                row[x][digit] = False
                col[y][digit] = False
                box[boxIndex(x, y)][digit] = False
                if dfs(board):
                    return True
                # 还原现场
                row[x][digit] = True
                col[y][digit] = True
                box[boxIndex(x, y)][digit] = True
                board[x][y] = '.'
            return False
        
        dfs(board)


class TestSolveSudoKu:

    """
    pytest -s 37_sudoku_solver.py::TestSolveSudoKu
    """

    def test(self):
        solution = Solution()

        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

        solution.solveSudoku(board)

        assert [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]
        ] == board 
