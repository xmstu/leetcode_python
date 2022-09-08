# -*- coding:utf-8 -*-
from typing import List


class DisjointSet:
    """
    并查集

    find 将 x 和 x 的所有祖先连在根节点上, 因此树的高度只有2层
    unionSet 把两棵树进行合并, 只有当两个节点的最高层级的祖先不一致时, 才合并
    """

    def __init__(self, n) -> None:
        self.fa = [i for i in range(n)]
    
    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def unionSet(self, x, y):
        self.fa[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def calc(self, sources: List[str], queries: List[str]) -> List[int]:
        # 用字典记录每个数对于父亲的比例
        parent_rate_map = {num: 1 for num in range(26)}
        results = []
        def convert_str_to_int(s: str):
            return ord(s) - ord("a")
        # 构建并查集
        disjointSet = DisjointSet(n=26)
        for source in sources:
            source_list = source.split(" ")
            dividend = source_list[0]
            divisor = source_list[2]
            quotient = float(source_list[4])
            dividend_num, divisor_num = convert_str_to_int(dividend), convert_str_to_int(divisor)
            disjointSet.unionSet(divisor_num, dividend_num)
            # 计算每个数对于父亲数字的比例
            last_rate = 1
            if disjointSet.find(dividend_num) != dividend_num:
                last_rate = parent_rate_map[dividend_num]
            parent_rate_map[divisor_num] = (1 / quotient) * last_rate
        
        for query in queries:
            query_list = query.split(" ")
            dividend = query_list[0]
            divisor = query_list[2]
            dividend_num, divisor_num = convert_str_to_int(dividend), convert_str_to_int(divisor)
            # 如果 被除数 和 除数 没有共同父亲, 就说明无法得到结果
            if not disjointSet.connected(dividend_num, divisor_num):
                results.append(-1)
                continue
            # 计算两个数的商, 通过字典获得当前 被除数 和 除数 对于 父亲数字 的比例, 两者相除得到结果
            results.append(parent_rate_map[dividend_num] / parent_rate_map[divisor_num])

        return results


class TestDivisionCalculate:

    """
    pytest -s division_calculate.py::TestDivisionCalculate
    """

    def test(self):
        solution = Solution()

        sources = ["a / b = 2", "b / c = 3", "a / d = 2", "e / f = 5", "b / g = 12"]
        queries = ["a / b", "a / c", "d / c", "a / e", "b / a", "a / g"]
        assert [2, 6, 3, -1, 0.5, 24] == solution.calc(sources, queries)
