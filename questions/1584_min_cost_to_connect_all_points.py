# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    给你一个points 数组, 表示 2D 平面上的一些点，其中 points[i] = [xi, yi]。
    连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 : |xi - xj| + |yi - yj|，其中 |val|表示 val的绝对值。
    请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

    Kruskal 算法总是使用并查集维护无向图的最小生成森林
    1. 建立并查集, 每个点格子构成一个集合
    2. 把所有边按照权值从小到大排序, 依次扫描每条边(x,y,z)
    3. 若 x,y 属于同一集合(连通), 则忽略这条边, 继续扫描下一条
    4. 否则, 合并 x,y 所在集合, 把 z 累加到答案中
    5. 所有边扫描完成后, 第四步中处理过的边就构成最小生成树
    时间复杂度 O(m *log m)
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 构造出边
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                edges.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        # 按边权排序
        edges.sort(key=lambda e: e[2])
        # kruskal 算法
        self.fa = []
        for i in range(n):
            self.fa.append(i)
        ans = 0
        for e in edges:
            x, y, z = self.find(e[0]), self.find(e[1]), e[2]
            if x != y:
                self.fa[x] = y
                ans += z
        return ans
    
    def find(self, x):
        # todo 并查集
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]


class TestMinCostConnPoints:

    """
    pytest -s 1584_min_cost_to_connect_all_points.py::TestMinCostConnPoints
    """

    def test(self):
        solution = Solution()

        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        assert 20 == solution.minCostConnectPoints(points)

        points = [[3,12],[-2,5],[-4,1]]
        assert 18 == solution.minCostConnectPoints(points)

        points = [[0,0],[1,1],[1,0],[-1,1]]
        assert 4 == solution.minCostConnectPoints(points)

        points = [[-1000000,-1000000],[1000000,1000000]]
        assert 4000000 == solution.minCostConnectPoints(points)

        points = [[0,0]]
        assert 0 == solution.minCostConnectPoints(points)

