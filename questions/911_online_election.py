# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # 预计算, 计算每个时刻领先的候选人数组
        # 该数组和时刻数组一一对应，到时候查找 t 时刻的领先候选人时, 二分查找 时刻数组即可
        tops = []
        voted_count_map = defaultdict(int)
        # 维护 top 变量, 
        top = -1
        voted_count_map[-1] = -1
        for person in persons:
            voted_count_map[person] += 1
            # 大于等于就解决了同票情况下, 谁是最近的投票人胜出的问题
            if voted_count_map[person] >= voted_count_map[top]:
                top = person
            tops.append(top)
        self.tops = tops
        self.times = times


    def q(self, t: int) -> int:
        # 找前驱
        left, right = -1, len(self.times) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        
        return self.tops[right]


class TestVote:

    """
    pytest -s 911_online_election.py::TestVote
    """

    def test(self):

        top_voted_candidate = TopVotedCandidate(
            persons=[0, 1, 1, 0, 0, 1, 0],
            times=[0, 5, 10, 15, 20, 25, 30]
        )

        assert 0 == top_voted_candidate.q(t=3)
        assert 1 == top_voted_candidate.q(t=12)
        assert 1 == top_voted_candidate.q(t=25)
        assert 0 == top_voted_candidate.q(t=15)
        assert 0 == top_voted_candidate.q(t=24)
        assert 1 == top_voted_candidate.q(t=8)

