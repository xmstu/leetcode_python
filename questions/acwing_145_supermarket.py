# -*- coding:utf-8 -*-
from typing import List
import sys


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


class Solution:

    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: x[0])

        # 用并查集
        disjoinSet = DisjointSet(3)

        # 求解
        ans = 0
        for i in range(n - 1, -1, -1):
            profit = nums[i][0]
            day = nums[i][1]
            # 关键在于 find , 过期日 day 已经卖出了产品的, 更新公共father
            lastAvailiabeDay = disjoinSet.find(day)
            if lastAvailiabeDay > 0:
                ans += profit
                disjoinSet.fa[lastAvailiabeDay] = lastAvailiabeDay - 1
        
        return ans


class TestMaxProfit:

    """
    pytest -s acwing_145_supermarket.py::TestMaxProfit
    """

    def test(self):
        solution = Solution()

        nums = [[50, 2], [10, 1], [20, 2], [30, 1]]
        assert 80 == solution.maxProfit(nums)

        nums = [[20, 1], [2, 1], [10, 3], [100, 2], [8, 2], [5, 20], [50, 10]]
        assert 185 == solution.maxProfit(nums)


if __name__ == "__main__":
    solution = Solution()
    # Read all integers into a list.
    allInputNums = []
    for line in sys.stdin:
        for num in line.split():
            allInputNums.append(int(num))
    
    # Parse list to get N and N items.
    readIndex = 0
    while readIndex < len(allInputNums):
        n = allInputNums[readIndex]
        nums = []
        for i in range(n):
            nums.append([allInputNums[readIndex + 2 * i + 1], allInputNums[readIndex + 2 * i + 2]])
        readIndex += 2 * n + 1

        ans = solution.maxProfit(nums) 
        print(ans)
