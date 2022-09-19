# -*- coding:utf-8 -*-
from typing import List
from functools import cache

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

    """
    除法式运算: https://docs.qq.com/doc/DYkZqY2paZVRhS1l2
    题目内容：
    输入：
    Sources：N个给定除法式。格式为 A / B = C, 其中A,B为字符串，C为浮点数，且C>0
    Queries：M个待计算除法式。格式为 A / B
    输出：
    计算后的M个除法式的结果，无法计算时返回-1。
    """

    def calc(self, sources: List[str], queries: List[str]) -> List[int]:
        # 用字典记录每个数对于父亲的比例
        parent_rate_map = {num: [num, 1] for num in range(26)}
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
            # 将被除数和除数归为同一父亲
            disjointSet.unionSet(divisor_num, dividend_num)
            # 记录每个除数的 【被除数】 和 【除数 对于 被除数 的比例】
            parent_rate_map[divisor_num] = [dividend_num, 1 / quotient]

        @cache
        def get_rate(num):
            """
            递归获取除数对于最终父亲的比例
            """
            dividend_num, rate = parent_rate_map[num]
            # 递归终止条件
            if num == dividend_num:
                return rate
            else:
                return rate * get_rate(dividend_num)

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
            dividend_rate = get_rate(dividend_num)
            divisor_rate = get_rate(divisor_num)
            results.append(dividend_rate / divisor_rate)

        return results


class TestDivisionCalculate:

    """
    pytest -s division_calculate.py::TestDivisionCalculate
    """

    def test(self):
        solution = Solution()

        sources = ["b / c = 3", "a / d = 2", "e / f = 5", "a / b = 2", "b / g = 12"]
        queries = ["a / b", "a / c", "d / c", "a / e", "b / a", "a / g"]
        assert [2, 6, 3, -1, 0.5, 24] == solution.calc(sources, queries)
