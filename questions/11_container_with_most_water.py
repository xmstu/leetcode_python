# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针思路:
            哪个小, 就用哪个乘以宽度, 小的那个指针移动
            左指针对应的数字小, 左指针 + 1, 
            右指针对应的数字小, 右指针 - 1
        """
        ans = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            if height[left] < height[right]:
                min_height = height[left]
                left += 1
            else:
                min_height = height[right]
                right -= 1
            ans = max(ans, min_height * width)
        return ans


class TestMaxArea:

    """
    pytest -s 11_container_with_most_water.py::TestMaxArea
    """

    def test(self):
        solution = Solution()

        height = [1,8,6,2,5,4,8,3,7]
        assert 49 == solution.maxArea(height)

        height = [1,1]
        assert 1 == solution.maxArea(height)
