# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        有这几种情况, 会存在多出一条附加边并出环的情况
            1. 没有入度为2的点, 但是某个点既存在出度和入度, 就一定有环
            2. 存在入度为2的点
                - 指向入度为2的点的那个点, 本身有入度, 删掉也无妨
                - 如果有环, 优先级就最高, 一定不对
        """
        n = len(edges)
        # 初始化入度数组
        ins = [0 for _ in range(n + 1)]
        # 初始化出度数组
        outs = [0 for _ in range(n + 1)]
        # 初始化邻接表
        adj = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        # 答案数组
        res = None

        # 记录入度为2的点
        inIsTwo = -1
        for edge in edges:
            from_point = edge[0]
            to_point = edge[1]
            # 将 to 结点的入度 + 1
            ins[to_point] += 1
            # 将 from 结点的出度 + 1
            outs[from_point] += 1
            # 将邻接表的相关位置变为 true
            adj[from_point][to_point] = True
        
            # 记录入度为2的节点
            if ins[to_point] == 2:
                inIsTwo = to_point
            
            # 在没有入度为2的点的情况下
            # 任意点, 只要入度和出度同时不为0, 必有环, 记录最后一条边
            if ins[to_point] == 1 and outs[to_point] > 0:
                res = edge
        
        # 有入度为2的点
        if inIsTwo != -1:
            res = None
            # 找指向 inIsTwo 的边
            # 这条边的 from, 既有出度, 又有入度, 说明有环
            for i in range(n - 1, -1, -1):
                from_point = edges[i][0]
                to_point = edges[i][1]
                if to_point == inIsTwo and outs[from_point] + ins[from_point] > 1:
                    if res == None:
                        res = edges[i] 
                    # 互相指向的场景
                    if adj[to_point][from_point]:
                        return edges[i]
    
        return res


class TestFindRedundantDirectedConnection:

    """
    pytest -s 685_redundant_connection_2.py::TestFindRedundantDirectedConnection
    """

    def test(self):
        solution = Solution()

        edges = [[1,2], [1,3], [2,3]]
        assert [2,3] == solution.findRedundantDirectedConnection(edges)

        edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        assert [1,4] == solution.findRedundantDirectedConnection(edges)

        edges = [[1,2],[2,3],[1,5],[3,4],[1,4]]
        assert [1,4] == solution.findRedundantDirectedConnection(edges)
