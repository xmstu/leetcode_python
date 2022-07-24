# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    树可以看成是一个连通且 无环 的 无向 图。
    给定往一棵 n 个节点 (节点值 1~n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。
    图的信息记录于长度为 n 的二维数组 edges, edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。
    请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。
    如果有多个答案，则返回数组 edges 中最后出现的边。
    """
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

    def connected(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


class SolutionDisjointSet:

    """
    思路:
        例子: edges = [[1,2], [1,3], [2,3]]
        利用并查集, 在每次遍历的时候划分分组,
        第一次遍历, edge: [1, 2], 1 归为 2 这个帮派
        第二次遍历, edge: [1, 3], 1 的父亲是 2, 2 和 3 组成更大的帮派, 此时, 2 的 父亲变为 3
        第三次遍历, edge: [2, 3], 2 的父亲是 3, 3 的父亲是自己, 已经连接了, 因此 [2, 3] 为冗余边
    """
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        disjointSet = DisjointSet(n+1)
        for i in range(n):
            print(f"before fa: {disjointSet.fa}")
            # 提前判断是否相连, 
            if disjointSet.connected(edges[i][0], edges[i][1]):
                return edges[i]
            else:
                disjointSet.unionSet(edges[i][0], edges[i][1])
            print(f"after fa: {disjointSet.fa}")
        
        return []


class TestFindRedundantConnection:

    """
    pytest -s 684_redundant_connection.py::TestFindRedundantConnection
    """

    def test(self):
        solution = SolutionDisjointSet()

        edges = [[1,2], [1,3], [2,3]]
        assert [2,3] == solution.findRedundantConnection(edges)

        edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        assert [1,4] == solution.findRedundantConnection(edges)

        edges = [[1,2],[2,3],[1,5],[3,4],[1,4]]
        assert [1,4] == solution.findRedundantConnection(edges)

        edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
        assert [4,5] == solution.findRedundantConnection(edges)


