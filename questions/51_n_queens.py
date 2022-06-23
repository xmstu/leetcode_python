# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
    n皇后问题 研究的是如何将 n个皇后放置在 n x n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
    每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                print("queens: %s, board: %s" % (queens, board))
                solutions.append(board)
            else:
                for i in range(n):
                    # 用三个集合做去重, columns 集合, 主对角线 集合, 副对角线 集合
                    # 主对角线: 同一条斜线上的每个位置满足行下标与列下标之差相等，例如 (0,0) 和 (3,3) 在的斜线上。因此使用行下标与列下标之差即可明确表示主对角线。
                    # 副对角线: 同一条斜线上的每个位置满足行下标与列下标之和相等，例如 (1,1) 和 (0,2) 在的斜线上。因此使用行下标与列下标之和即可明确表示副对角线。
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    # queens 的 下标索引 就是 行数, i 是列数, 这样就代表该皇后 占据了 [i, j] 位置
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                    
        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions
        

class TestNQueens:

    """
    pytest -s 51_n_queens.py::TestNQueens
    """

    def test(self):
        solution = Solution()

        assert [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] == solution.solveNQueens(n=4)

        assert [["Q"]] == solution.solveNQueens(n=1)
