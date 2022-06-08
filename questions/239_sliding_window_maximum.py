# -*- coding:utf-8 -*-
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        利用单调递减的队列去除冗余的候选项
        滑动窗口从左向右移动, 新的数是递减的, 那么就保留, 如果新的数比之前的大, 之前的数必然无法成为候选的最大值, 并且生命周期还短
        """
        ans = []
        # 数组模拟双端队列, 存下标(代表时间)
        l, r = 0, -1
        q = [0] * len(nums)
        for i in range(len(nums)):
            # 保证队头合法性
            while l < r and q[l] <= i - k:
                l += 1
            # 维护队列单调性, 插入新的选项
            while l <= r and nums[q[r]] <= nums[i]:
                r -= 1
            r += 1
            q[r] = i
            # 取队头更新答案
            if i >= k - 1:
                ans.append(nums[q[l]])
            
        return ans
    
    def maxSlidingWindowDeque(self, nums: List[int], k: int) -> List[int]:
        print("nums: %s" % nums)
        ans = []
        # 下标(时间)递增, 值递减的队列
        q = deque()
        for index, value in enumerate(nums):
            # 删除出界的选项
            while len(q) > 0 and q[0] <= index - k:
                print("q[0]: %s, index: %s, k: %s" % (q[0], index, k))
                q.popleft()
            # 插入新选项i, 维护单调性(值递减)
            while len(q) > 0 and nums[q[-1]] <= value:
                print("q[-1]: %s, nums[q[-1]]: %s, value: %s" % (q[-1], nums[q[-1]], value))
                q.pop()
            q.append(index)
            print("q: %s" % q)
            # 取队头更新答案
            if index >= k - 1:
                print("index: %s, k - 1: %s" % (index, k - 1))
                ans.append(nums[q[0]])
                print("ans: %s" % ans)
        
        print()
        
        return ans


class TestMaxSlidingWindow:

    """
    pytest -s 239_sliding_window_maximum.py::TestMaxSlidingWindow
    """

    def test(self):
        solution = Solution()

        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        assert [3,3,5,5,6,7] == solution.maxSlidingWindowDeque(nums, k)

        nums = [1] 
        k = 1
        assert [1] == solution.maxSlidingWindowDeque(nums, k)
