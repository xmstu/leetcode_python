# -*- coding:utf-8 -*-
from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        to = [[] for _ in range(numCourses)]
        # 入度数组, 入度代表每个点有多少条入边
        inDeg = [0 for _ in range(numCourses)]
        for pre in prerequisites:
            ai, bi = pre[0], pre[1]
            to[bi].append(ai)
            inDeg[ai] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDeg[i] == 0:
                q.appendleft(i)

        lessons = []
        while q:
            x = q.pop()
            lessons.append(x)
            for y in to[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.appendleft(y)
        
        return len(lessons) == numCourses

class TestCanFinsh:

    """
    pytest -s 207_course_schedule.py::TestCanFinsh
    """

    def test(self):
        solution = Solution()

        numCourses, prerequisites = 2, [[1,0]]
        assert True == solution.canFinish(numCourses, prerequisites)

        numCourses, prerequisites = 2, [[1,0], [0,1]]
        assert False == solution.canFinish(numCourses, prerequisites)
