# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 基于计数排序
        ans = []
        upper = max(arr1)
        count = [0] * (upper + 1)
        for val in arr1:
            count[val] += 1
        
        for val in arr2:
            while count[val]:
                ans.append(val)
                count[val] -= 1
        
        # 最后扫一遍 count 中不为0 的下标对应还有多少个数, 加进去 ans
        for val in range(upper + 1):
            while count[val]:
                ans.append(val)
                count[val] -= 1
        
        return ans


class TestRelativeSortArray:

    """
    pytest -s 1122_relative_sort_array.py::TestRelativeSortArray
    """

    def test(self):
        solution = Solution()

        arr1 = [2,3,1,3,2,4,6,7,9,2,19]; arr2 = [2,1,4,3,9,6]
        assert [2,2,2,1,4,3,3,9,6,7,19] == solution.relativeSortArray(arr1, arr2)

        arr1 = [28,6,22,8,44,17]; arr2 = [22,28,8,6]
        assert [22,28,8,6,17,44] == solution.relativeSortArray(arr1, arr2)
