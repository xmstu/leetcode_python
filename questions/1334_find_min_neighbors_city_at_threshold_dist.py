# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    有 n 个城市, 按从 0 到 n-1 编号。给你一个边数组 edges,
    其中 edges[i] = [fromi, toi, weighti] 代表 fromi 和 toi 两个城市之间的双向加权边，
    距离阈值是一个整数 distanceThreshold。
    返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。
    如果有多个这样的城市, 则返回编号最大的城市。
    注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。

    floyd 算法求解, 将 i 和 j 的最短路径转为 i -> k 和 k -> j 的路径和的子问题, k 是中继节点
    遍历每个中继点, 就可以求出每个 i -> j 的最短路径的长度
    """
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[1e9] * n for _ in range(n)]
        # 对角线的位置初始化为0
        for i in range(n):
            d[i][i] = 0
        # 初始化邻接矩阵
        for edge in edges:
            x = edge[0]
            y = edge[1]
            z = edge[2]
            d[x][y] = d[y][x] = z
        # floyd算法, relay 是中继节点的意思
        for relay in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][relay] + d[relay][j])
        
        # 根据题意统计
        minNeighbor = 1e9
        ans = 0
        for i in range(n):
            neighbor = 0
            for j in range(n):
                # i -> j 路径和小于等于阈值, 邻居 +1
                if i != j and d[i][j] <= distanceThreshold:
                    neighbor += 1
            # 更新 minNeighbor 和 ans
            if neighbor < minNeighbor or (neighbor == minNeighbor and i > ans):
                minNeighbor = neighbor
                ans = i
        return ans



class TestFindCity:

    """
    pytest -s 1334_find_min_neighbors_city_at_threshold_dist.py::TestFindCity
    """

    def test(self):
        solution = Solution()

        n = 4; edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]; distanceThreshold = 4
        assert 3 == solution.findTheCity(n, edges, distanceThreshold)

        n = 5; edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]; distanceThreshold = 2
        assert 0 == solution.findTheCity(n, edges, distanceThreshold)
