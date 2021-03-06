# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 给区间排序, 先按区间左值升序排序, 如果左值相等, 再按右值升序排序
        intervals.sort(key=lambda interval: (interval[0], interval[1]))

        ans = []
        farthest = -1
        start = -1
        for interval in intervals:
            left = interval[0]
            right = interval[1]
            # 遇到左值比右值大, 说明连续的区间结束, 到了新区间
            if left <= farthest:
                farthest = max(farthest, right)
            else:
                if farthest != -1:
                    ans.append([start, farthest])
                start = left
                farthest = right
        ans.append([start, farthest])
        
        return ans


class SolutionDiff:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        把从1覆盖到5这个区间，看作2个事件：
        (a) 在1处，有一个事件：开始覆盖（次数+1）
        (b) 在5+1处，有一个事件：结束覆盖（次数-1）

        然后 差分事件排序
        """
        ans = []
        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))
        
        events.sort()
        print("events: %s" % events)
        covering = 0
        start = 0
        for event in events:
            if covering == 0:
                start = event[0]
            covering += event[1]
            if covering == 0:
                ans.append([start, event[0] - 1])
        
        return ans


class TestMerge:

    """
    pytest -s 56_merge_intervals.py::TestMerge
    """

    def test(self):
        solution = SolutionDiff()

        intervals = [[1,3],[2,6],[8,10],[15,18]]
        assert [[1,6],[8,10],[15,18]] == solution.merge(intervals)

        intervals = [[1,4],[4,5]]
        assert [[1,5]] == solution.merge(intervals)

        intervals = [[1,4],[0,4]]
        assert [[0,4]] == solution.merge(intervals)
