# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

    注意：

    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。
    空白格用 '.' 表示。

    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        思路: 用集合记录 9 行, 9 列 和 9 个 方格是否出现过重复数字, 注意 python 集合是可变对象, 不能 row_sets = [set()] * 9
        """
        row_sets = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        col_sets = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 
        box_sets = [set(), set(), set(), set(), set(), set(), set(), set(), set()] 

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == '.':
                    continue
                if digit in row_sets[i]:
                    return False
                if digit in col_sets[j]:
                    return False
                k = (i // 3) * 3 + j // 3
                if digit in box_sets[k]:
                    return False
                row_sets[i].add(digit)
                col_sets[j].add(digit)
                box_sets[k].add(digit)

        return True


class TestIsValidSudoKu:

    """
    pytest -s 36_valid_sudoku.py::TestIsValidSudoKu
    """

    def test(self):
        solution = Solution()

        board = [
             ["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]
        assert True == solution.isValidSudoku(board)

        board = [
             ["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]
        assert False == solution.isValidSudoku(board)

