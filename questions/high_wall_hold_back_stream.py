# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:

    """
    高墙挡水问题: https://docs.qq.com/doc/DYlpSaWZOZ2NyR1N0
    左边是水，中间是高墙，右边是城市, 求高墙能阻挡的最高水位, 因为水是从左向右流, 左边的第一列为起点，右边的最后一列为终点
    """

    def water_level(self, walls: List[List[int]]):
        m, n = len(walls), len(walls[0])

        # 方向数组
        Dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 获取起点和终点
        start_point = (0, 0)
        end_points = []
        # 获取最低墙高和最高墙高作为二分查找的上下限
        left, right = float("inf"), -1
        for row in range(m):
            if walls[row][0] < walls[start_point[0]][0]:
                start_point = (row, 0)
            end_points.append((row, n - 1))
            for col in range(n):
                left = min(left, walls[row][col])
                right = max(right, walls[row][col])
        
        def in_area(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def bfs(water_level: int):
            q = deque()
            q.appendleft(start_point)
            visted = [[False] * n for _ in range(m)]
            visted[start_point[0]][start_point[1]] = True

            while q:
                x, y = q.pop()
                # 向上下左右遍历, 如果当前的水位能顺利到达终点, 就返回True, 否则返回False
                for dx, dy in Dir:
                    nx = x + dx
                    ny = y + dy
                    if not in_area(nx, ny) or visted[nx][ny]:
                        continue
                    if walls[nx][ny] <= water_level:
                        if (nx, ny) in end_points:
                            return True
                        q.appendleft((nx, ny))
                        visted[nx][ny] = True
        
            return False
        
        
        # 二分答案求解, bfs作为验证的函数
        while left < right:
            mid = (left + right) // 2
            if bfs(water_level=mid):
                right = mid
            else:
                left = mid + 1
        
        return right
        


class TestHighWallHoldBackStream:

    """
    pytest -s high_wall_hold_back_stream.py::TestHighWallHoldBackStream
    """

    def test(self):
        solution = Solution()

        walls = [
            [9, 7, 5, 3, 1],
            [2, 4, 6, 8, 6],
            [1, 3, 4, 2, 3],
            [6, 2, 1, 4, 8],
        ]

        assert 4 == solution.water_level(walls)
