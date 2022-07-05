
# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        self.m = len(maze)
        self.n = len(maze[0])

        maze[start[0]][start[1]] = 2

        self.Bool = False
        self.destination = destination

        self.dfs(start[0], start[1], maze)

        return self.Bool

    def dfs(self, x0, y0, maze):

        if self.Bool == True:
            return


        Dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for dir in Dir:
            x = x0
            y = y0

            while(0 <= x < self.m and 0 <= y < self.n and maze[x][y] != 1):
                x += dir[0]
                y += dir[1]

            x -= dir[0]
            y -= dir[1]

            if x == self.destination[0] and y == self.destination[1]:
                self.Bool = True
                return

            if maze[x][y] == 0:
                maze[x][y] = 2
                self.dfs(x, y, maze)


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])

        Q = deque()     
        Q.append(start)

        Dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while(Q):

            x0, y0 = Q.popleft()

            for dir in Dir:
                x = x0 + dir[0]
                y = y0 + dir[1]

                while (x >= 0 and x < m and y >= 0 and y < n and maze[x][y] != 1):
                    x += dir[0]
                    y += dir[1]

                x = x - dir[0]
                y = y - dir[1]

                if x == destination[0] and y == destination[1]:
                    return True

                if maze[x][y] == 0:
                    Q.append((x, y))
                    maze[x][y] = 2

        return False


class TestHasPath:

    """
    pytest -s 490_maze.py::TestHasPath
    """

    def test(self):
        solution = Solution()

        maze = [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ]; start = [0,4]; destination = [4,4]
        ans = solution.hasPath(maze, start, destination)

        maze = [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]]; start = [0,4]; destination = [3,2]
        assert False == solution.hasPath(maze, start, destination)

        maze = [
            [0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]]; start = [4,3]; destination = [0,1]
        assert False == solution.hasPath(maze, start, destination)
        
