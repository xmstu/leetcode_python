
# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
    省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
    给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
    返回矩阵中 省份 的数量。

    思路: 
        利用并查集将连在一起的城市归为一个集合, 最后统计有多少个城市的父亲是它自己本身的, 就有多少个省份
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # MakeSet
        fa = []
        for i in range(n):
            fa.append(i)
        
        def find(x: int):
            if x == fa[x]:
                return x
            fa[x] = find(fa[x])
            return fa[x]
        
        def unionSet(x: int, y: int):
            x = find(x)
            y = find(y)
            if x != y:
                fa[x] = y

        # 对于每条边, 把两个集合合并
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    unionSet(i, j)
        ans = 0
        for i in range(n):
            if find(i) == i:
                ans += 1
        return ans



class TestFindCircleNum:

    """
    pytest -s 547_number_of_provinces.py::TestFindCircleNum
    """

    def test(self):
        solution = Solution()

        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        assert 2 == solution.findCircleNum(isConnected)

        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        assert 3 == solution.findCircleNum(isConnected)
