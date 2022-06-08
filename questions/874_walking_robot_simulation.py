# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        # 机器人最开始从 (0, 0) 出发
        x, y =0, 0
        # 最大距离
        ans = 0
        # 网格中行走题目, 技巧: 方向数组
        # 向北走是 (0, 1), 向东走是 (1, 0), 向南走是 (0, -1), 向西走是 (-1, 0)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        # 方向变量 direction, N=0, E=1, S=2, W=3
        # 机器人初始化是原点面向北方
        direction = 0
        for command in commands:
            # 右转
            if command == -1:
                direction = (direction + 1) % 4
            # 左转
            elif command == -2:
                direction = (direction + 3) % 4
            else:
                for _ in range(command):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    # 如果遇到障碍物, 停止, 不更新 x, y
                    if (nx, ny) in obs:
                        break
                    # 走了 command 步后, 没遇到障碍物, 更新 x, y
                    x, y = nx, ny
                    # 更新走的最大距离
                    ans = max(ans, x * x + y * y)

        return ans


class TestRobotSim:

    """
    pytest -s 874_walking_robot_simulation.py::TestRobotSim
    """

    def test(self):
        solution = Solution()

        commands = [4,-1,3]
        obstacles = []
        assert 25 == solution.robotSim(commands, obstacles)

        commands = [4,-1,4,-2,4]
        obstacles = [[2,4]]
        assert 65 == solution.robotSim(commands, obstacles)


