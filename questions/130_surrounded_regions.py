# -*- coding:utf-8 -*-
from collections import deque
from typing import List

class SolutionDfs:

    """
    给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_area(x, y):
            return 0 <= x < nrow and 0 <= y < ncol

        def dfs(x, y):
            # 递归边界
            if board[x][y] in ("X", "B"):
                return
            
            # 每层要做的事
            # 将和边界连通的改为 B
            board[x][y] = "B"
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not in_area(nx, ny):
                    continue
                dfs(nx, ny)

        # 从边界开始dfs
        for col in range(ncol):
            dfs(0, col)
            dfs(nrow - 1, col)
        for row in range(nrow):
            dfs(row, 0)
            dfs(row, ncol - 1)
        
        # 遍历一遍矩阵, 将所有是 B 的还原为 O, 再将所有是 O 的改为 X
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == "B":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        
class SolutionBfs:

    """
    给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
    """
    def solve(self, board: List[List[str]]) -> None:
        nrow, ncol = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def in_area(x, y):
            return 0 <= x < nrow and 0 <= y < ncol

        q = deque()
        # 从边界开始遍历
        for col in range(ncol):
            if board[0][col] == "O":
                q.appendleft((0, col))
            if board[nrow - 1][col] == "O":
                q.appendleft((nrow - 1, col))
        for row in range(nrow):
            if board[row][0] == "O":
                q.appendleft((row, 0))
            if board[row][ncol - 1] == "O":
                q.appendleft((row, ncol - 1))
        
        # 广度优先遍历
        while q:
            row, col  = q.pop()
            board[row][col] = "B"
            for dx, dy in DIRS:
                nx, ny = row + dx, col + dy
                if not in_area(nx, ny):
                    continue
                if board[nx][ny] in ("X", "B"):
                    continue
                q.appendleft((nx, ny))

         # 遍历一遍矩阵, 将所有是 B 的还原为 O, 再将所有是 O 的改为 X
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == "B":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"


class DisjointSet:
	"""
	并查集

	find 将 x 和 x 的所有祖先连在根节点上, 因此树的高度只有2层
	unionSet 把两棵树进行合并, 只有当两个节点的最高层级的祖先不一致时, 才合并
	"""

	def __init__(self, n) -> None:
		self.fa = [i for i in range(n)]
	
	def find(self, x):
		if x == self.fa[x]:
			return x
		self.fa[x] = self.find(self.fa[x])
		return self.fa[x]
	
	def unionSet(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x != y:
			self.fa[x] = y


class SolutionDisjointSet:

    """
    并查集思路
        1. 将边界的 O 和 连着边界的 O 和 一个 虚拟的 外界点相连, 作为一个集;
        2. 被 X 包围的 O 归为另一个集合, 在最后判断 O 点的父亲不是 outside 的就赋值为 X;
    """

    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        disjointSet = DisjointSet(m * n + 1)
        outside = m * n
        Dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def num(i, j):
            return i * n + j
        
        def in_area(x, y):
            return 0 <= x < m and 0 <= y < n
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                for dx, dy in Dir:
                    ni, nj = i + dx, j + dy
                    # 超出边界, 说明 (i, j) 是 边界点, 并且 board[i][j] = 'O', 将该点和 outside 相连
                    if not in_area(ni, nj):
                        disjointSet.unionSet(num(i, j), outside)
                    else:
                        # 与边界相连的 O 归为一组, 被 X 包围的 O 归为一组
                        if board[ni][nj] == 'O':
                            disjointSet.unionSet(num(i, j), num(ni, nj))

        # 找出所有与 外界点 不相连的 O, 改为 X
        the_outside = disjointSet.find(outside)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and disjointSet.find(num(i, j)) != the_outside:
                    board[i][j] = 'X' 

class TestSolve:

    """
    pytest -s 130_surrounded_regions.py::TestSolve
    """

    def test(self):

        solution = SolutionDisjointSet()

        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]

        solution.solve(board)
        """
        被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
        任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
        如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
        """
        assert [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ] == board

        board = [["X"]]
        solution.solve(board)
        assert [["X"]] == board

        board = [["O","O","O"],["O","O","O"],["O","O","O"]]
        solution.solve(board)
        assert [["O","O","O"],["O","O","O"],["O","O","O"]] == board
