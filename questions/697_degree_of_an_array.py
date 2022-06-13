# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        记原数组中出现次数最多的数为 x 那么和原数组的度相同的最短连续子数组，必然包含了原数组中的全部 x 且两端恰为 x 第一次出现和最后一次出现的位置。
        因为符合条件的 x 可能有多个，即多个不同的数在原数组中出现次数相同。所以为了找到这个子数组，我们需要统计每一个数出现的次数，同时还需要统计每一个数第一次出现和最后一次出现的位置。
        在实际代码中，我们使用哈希表实现该功能，每一个数映射到一个长度为 3 的数组，数组中的三个元素分别代表这个数出现的次数、这个数在原数组中第一次出现的位置和这个数在原数组中最后一次出现的位置。当我们记录完所有信息后，我们需要遍历该哈希表，找到元素出现次数最多，且前后位置差最小的数。

        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
        最短子数组的长度取决于最大频数第一次出现的位置和最后一次出现的位置
        """
        num_map = {}
        for index, num in enumerate(nums):
            if num in num_map.keys():
                num_map[num][0] += 1
                num_map[num][2] = index
            else:
                num_map[num] = [1, index, index]

        degree = 0
        min_len = 0
        for count, left, right in num_map.values():
            if count > degree:
                degree = count
                min_len = right - left + 1
            elif degree == count:
                span = right - left + 1
                if min_len > span:
                    min_len = span
        
        return min_len

    def findShortestSubArray2(self, nums: List[int]) -> int:
        from collections import defaultdict
        counter = defaultdict(int)
        left_map, right_map = {}, {}
        
        for index, num in enumerate(nums):
            counter[num] += 1
            if num not in left_map:
                left_map[num] = index
            right_map[num] = index
        
        degree = max(counter.values())
        ans = len(nums)
        for num, cnt in counter.items():
            if cnt == degree:
                ans = min(ans, right_map[num] - left_map[num] + 1)
        return ans

class TestFindShortestSubArray:

    """
    pytest -s 697_degree_of_an_array.py::TestFindShortestSubArray
    """

    def test(self):
        solution = Solution()

        nums = [1,2,2,3,1]
        assert 2 == solution.findShortestSubArray(nums)

        nums = [1,2,2,3,1,4,2]
        assert 6 == solution.findShortestSubArray(nums)
