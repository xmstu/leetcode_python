# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-08-11
    :Copyright: (c) 2021, hexm
"""
from copy import deepcopy
from typing import List
from collections import deque


class SolutionDfs:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
        岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
        此外，你可以假设该网格的四条边均被水包围

        示例1:
        输入：grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        输出：1

        示例2:
        输入：grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        输出：3

        题解: https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/
        二叉树的DFS有两个要素：访问相邻结点 和 判断 base case
        但是网状结构本质上是图，一个节点从四个方向出发，有可能会重复遍历，因此还要加多一个步骤，遍历过的节点要做标记

        :param grid:
        :return:
        """
        new_grid = deepcopy(grid)


        def in_area(grid, r, c):
            """
            判断坐标 (r, c) 是否在网格中
            :param grid:
            :param r:
            :param c:
            :return:
            """
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(grid, r, c):
            # 深度优先搜索的时候，上下左右会超出网格的边界，超出边界的停止递归遍历
            if not in_area(grid, r, c):
                return
            # 遇到不是陆地的，停止递归遍历
            if grid[r][c] != "1":
                return

            # 每走过一个陆地格子，就把格子的值改为 2，这样当我们遇到 2 的时候，就知道这是遍历过的格子了，下次再遇到这个格子就停止遍历
            grid[r][c] = "2"

            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        num = 0
        for r, _ in enumerate(new_grid):
            for c, _ in enumerate(new_grid[0]):
                if new_grid[r][c] == "1":
                    num += 1
                    dfs(new_grid, r, c)
        return num

class SolutionBfs:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        广度优先搜索
        :param grid:
        :return:
        """
        new_grid = deepcopy(grid)
        nr = len(new_grid)
        if nr == 0:
            return 0
        nc = len(new_grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if new_grid[r][c] == "1":
                    num_islands += 1
                    new_grid[r][c] = "2"
                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and new_grid[x][y] == "1":
                                neighbors.append((x, y))
                                new_grid[x][y] = "2"

        return num_islands


class SolutionBfs2:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        广度优先搜索, 利用访问数组记录是否访问过
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.visit = [[False] * self.n for _ in range(self.m)]
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1' and not self.visit[i][j]:
                    ans += 1
                    self.bfs(grid, i, j)
        
        return ans
    
    def bfs(self, grid: List[List[str]], sx: int, sy: int):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        # 第一步, push 起点到队列中
        q = deque()
        q.appendleft([sx, sy])
        self.visit[sx][sy] = True
        while q:
            x, y = q.pop()
            # 扩展该点的上下左右的点
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 检查边界
                if not self.in_area(nx, ny):
                    continue
                if grid[nx][ny] == '1' and not self.visit[nx][ny]:
                    q.appendleft([nx, ny])
                    self.visit[nx][ny] = True
    
    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n


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
    利用并查集获取岛屿数量, 将岛屿各自划分为一组, 最终扫描 fa 数组, 看有多少个自己的父亲是自己的, 就有多少个岛屿
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        disjointSet = DisjointSet(m * n)
        Dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(m)]

        def in_area(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def num(x, y):
            return x * n + y
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                for dx, dy in Dir:
                    ni, nj = i + dx, j + dy
                    if not in_area(ni, nj):
                        continue
                    if visited[ni][nj]:
                        continue
                    # 将所有在同一岛屿的归为一组
                    if grid[ni][nj] == "1":
                        disjointSet.unionSet(num(ni, nj), num(i, j))
                visited[i][j] = True
        
        ans = 0
        for i in range(m):
            for j in range(n):
                fa_index = num(i, j)
                if grid[i][j] == "1" and disjointSet.find(fa_index) == fa_index:
                    ans += 1
        
        return ans
        

class TestNumberOfIslands(object):
    """
    pytest -s 200_the_number_of_islands.py::TestNumberOfIslands
    """

    def test_solution(self):
        solution = SolutionDisjointSet()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert 1 == solution.numIslands(grid)

        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert 3 == solution.numIslands(grid)
