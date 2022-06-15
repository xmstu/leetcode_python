# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for edge in edges:
            x, y = edge[0], edge[1]
            n = max(n, max(x, y))
        n = n + 1
        # 出边数组
        self.to = [[] for _ in range(n)]
        self.visited = [False for _ in range(n)]
        self.has_cycle = False
        for edge in edges:
            x, y = edge[0], edge[1]
            self.to[x].append(y)
            self.to[y].append(x)
            # 每次dfs完要记得初始化 visted 数组
            self.visited = [False for _ in range(n)]
            self.dfs(x, 0)
            if self.has_cycle:
                return edge

    def dfs(self, x: int, father: int):
        self.visited[x] = True

        for y in self.to[x]:
            if y == father:
                continue
            if not self.visited[y]:
                self.dfs(y, x)
            else:
                self.has_cycle = True


class TestFindRedundantConnection:

    """
    pytest -s 684_redundant_connection.py::TestFindRedundantConnection
    """

    def test(self):
        solution = Solution()

        edges = [[1,2], [1,3], [2,3]]
        assert [2,3] == solution.findRedundantConnection(edges)

        edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        assert [1,4] == solution.findRedundantConnection(edges)

        edges = [[1,2],[2,3],[1,5],[3,4],[1,4]]
        assert [1,4] == solution.findRedundantConnection(edges)

        edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
        assert [4,5] == solution.findRedundantConnection(edges)


