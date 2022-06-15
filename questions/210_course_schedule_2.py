# -*- coding:utf-8 -*-
from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            print("x: %s" % x)
            lessons.append(x)
            for y in to[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.appendleft(y)
        
        return lessons if len(lessons) == numCourses else []


class TestFindOrder:

    """
    pytest -s 210_course_schedule_2.py::TestFindOrder
    """

    def test(self):
        solution = Solution()

        numCourses, prerequisites = 2, [[1,0]]
        assert [0,1] == solution.findOrder(numCourses, prerequisites)

        numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
        assert [0,1,2,3] == solution.findOrder(numCourses, prerequisites)

        numCourses, prerequisites = 3, [[1,0],[1,2],[0,1]]
        assert [] == solution.findOrder(numCourses, prerequisites)
