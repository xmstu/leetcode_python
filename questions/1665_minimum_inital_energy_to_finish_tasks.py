# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个任务数组 tasks ，其中 tasks[i] = [actuali, minimumi] ：
    actuali 是完成第 i 个任务 需要耗费 的实际能量。
    minimumi 是开始第 i 个任务前需要达到的最低能量。
    比方说，如果任务为 [10, 12] 且你当前的能量为 11 ，那么你不能开始这个任务。如果你当前的能量为 13 ，你可以完成这个任务，且完成它后剩余能量为 3 。
    你可以按照 任意顺序 完成任务。
    请你返回完成所有任务的 最少 初始能量。
    """
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # 按照 actual - minimum 升序排序
        tasks.sort(key=lambda item: item[0] - item[1])
        ans = 0
        # 倒序遍历
        for i in range(len(tasks) - 1, -1, -1):
            # 看是门槛大还是耗费大, 谁大，谁更新成为 ans
            ans = max(tasks[i][1], ans + tasks[i][0])
        return ans


class TestMinimumEffort:

    """
    pytest -s 1665_minimum_inital_energy_to_finish_tasks.py::TestMinimumEffort
    """

    def test(self):
        solution = Solution()

        tasks = [[1,2],[2,4],[4,8]]
        assert 8 == solution.minimumEffort(tasks)

        tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
        assert 32 == solution.minimumEffort(tasks)

        tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
        assert 27 == solution.minimumEffort(tasks)

