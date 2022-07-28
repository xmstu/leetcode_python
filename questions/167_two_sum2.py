# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
    以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
    你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
    你所设计的解决方案必须只使用常量级的额外空间。

    双指针扫描, 比较两数之和 和 target值即可, 从而移动 i 或 j
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            two_sum = numbers[i] + numbers[j]
            if two_sum == target:
                return [i+1, j+1]
            elif two_sum < target:
                i += 1
            elif two_sum > target:
                j -= 1
        return []


class TestTwoSum:

    """
    pytest -s 167_two_sum2.py::TestTwoSum
    """

    def test(self):
        solution = Solution()

        numbers = [2,7,11,15]; target = 9
        assert [1, 2] == solution.twoSum(numbers, target)

        numbers = [2,3,4]; target = 6
        assert [1, 3] == solution.twoSum(numbers, target)

        numbers = [-1,0]; target = -1
        assert [1, 2] == solution.twoSum(numbers, target)
