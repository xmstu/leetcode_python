# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        暴力法, 直接硬移动
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                new = 0
                for j in range(i+1, n):
                    cur = arr[j]
                    arr[j] = new
                    new = cur
                i += 2
            else:
                i += 1


class Solution2:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        双指针
        """
        i, j, n = 0, 0, len(arr)
        while j < n:
            # 每次 i 对应的值是0, j 移动多一步
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        i -= 1
        j -= 1

        # 从后往前遍历, arr[j] = arr[i], 遇到 arr[i] = 0, 那么 arr[j-1] = 0, j -= 1 
        # 在上面 j 每遇到 0 多加一步, 这里就减多一步, 最终, i 和 j 会同时到 0
        while i >= 0:
            if j < n: 
                print("i: %s, j: %s, arr[i]: %s" % (i, j, arr[i]))
                arr[j] = arr[i]
            if arr[i] == 0 and j-1 >= 0:
                arr[j-1] = 0
                j -= 1
            j -= 1
            i -= 1


class TestDulicateZeros:

    """
    pytest -s 1089_duplicate_zeros.py::TestDulicateZeros
    """

    def test(self):
        solution = Solution2()

        arr = [1,0,2,3,0,4,5,0]
        solution.duplicateZeros(arr)
        assert [1,0,0,2,3,0,0,4] == arr

        arr = [1,2,3]
        solution.duplicateZeros(arr)
        assert [1,2,3] == arr
