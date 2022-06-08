# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
    请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
    """
    
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive_seq_length = 0
        nums_set = set(nums)
        for num in nums_set:
            print("num: %s" % num)
            # num - 1 not in nums_set，是为了减少循环次数，num - 1 的值在集合里面的就不用迭代了，num 必须是序列的最小值
            if num - 1 not in nums_set:
                curr_num = num
                print("curr num: %s" % curr_num)
                curr_length = 1
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_length += 1
            
                print("curr len: %s" % curr_length)
                longest_consecutive_seq_length = max(longest_consecutive_seq_length, curr_length)
        
        return longest_consecutive_seq_length


class TestLongestConsecutive(object):

    """
    pytest -s 128_longest_consecutive_sequence.py::TestLongestConsecutive
    """

    def test_longest_consecutive(self):
        solution = Solution()
        nums = [100,4,200,1,3,2]
        assert 4 == solution.longestConsecutive(nums)
        nums = [0,3,7,2,5,8,4,6,0,1]
        assert 9 == solution.longestConsecutive(nums)

