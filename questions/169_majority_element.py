# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    """
    def majorityElement(self, nums: List[int]) -> int:
        cnt_map = {}
        for num in nums:
            if num not in cnt_map:
                cnt_map[num] = 1
                continue
            cnt_map[num] += 1
        
        for num, cnt in cnt_map.items():
            if cnt > len(nums) / 2:
                return num
    
    def majorityElementDivideAndConquer(self, nums: List[int]) -> int:
        """
        将数组的状态空间一分为二, 将求当前数组的众数这个问题, 分拆成求左右两个子数组的众数,
        最后将两个子问题的答案, 归并起来, 决策出当前问题的众数
        """
        return self.majorityElementRecr(nums, 0, len(nums) - 1)
        pass
    
    def majorityElementRecr(self, nums: List[int], left: int, right: int):
        # 递归终止条件
        if left == right:
            return nums[left]
        
        # 每层要做的事
        mid = (right - left) // 2 + left
        left_major = self.majorityElementRecr(nums, left, mid)
        right_major = self.majorityElementRecr(nums, mid+1, right)

        if left_major == right_major:
            return left_major
        
        left_cnt = self.count_in_range(nums, left_major, left, right)
        right_cnt = self.count_in_range(nums, right_major, left, right)

        return left_major if left_cnt > right_cnt else right_major
    
    def count_in_range(self, nums, num, left, right):
        count = 0
        for i in range(left, right+1):
            if nums[i] == num:
                count += 1
        return count



class TestMajorityElement:

    """
    pytest -s 169_majority_element.py::TestMajorityElement
    """

    def test(self):
        solution = Solution()

        nums = [3,2,3]
        assert 3 == solution.majorityElement(nums)

        nums = [2,2,1,1,1,2,2]
        assert 2 == solution.majorityElement(nums)
