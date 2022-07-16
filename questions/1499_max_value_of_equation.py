# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution1:
    """
    给你一个数组 points: [(x1, y1), (x2, y2)], 求 yi + yj + |xi - xj| 的最大值 (i != j), 没有|xi - xj| < k的限制
    """

    def findMaxValueOfEquationVersion1(self, points: List[List[int]]) -> int:
        """
        朴素 O(n**2)
        """
        n = len(points)
        x = [0]
        y = [0]
        for point in points:
            x.append(point[0])
            y.append(point[1])
        
        print("x: %s" % x)
        print("y: %s" % y)

        ans = float("-inf")
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    ans = max(ans, y[i] + y[j] + abs(x[i] - x[j]))
        return ans

    def findMaxValueOfEquationVersion2(self, points: List[List[int]]) -> int:
        """
        优化, 因为是坐标上的点, x 是有序的, 因此让 j < i 即可, 同时可以取消绝对值运算, 减少运算量
        """
        n = len(points)
        x = [0]
        y = [0]
        for point in points:
            x.append(point[0])
            y.append(point[1])
        ans = float("-inf") 
        for i in range(2, n+1):
            for j in range(1, i):
                ans = max(ans, y[i] + y[j] + x[i] - x[j])

        return ans
    
    def findMaxValueOfEquationVersion3(self, points: List[List[int]]) -> int:
        """
        y[i] + x[i] 不随着 j 变化, 可以提出来计算
        """
        n = len(points)
        x = [0]
        y = [0]
        for point in points:
            x.append(point[0])
            y.append(point[1])
        ans = float("-inf") 
        for i in range(2, n+1):
            temp = float("-inf")
            for j in range(1, i):
                temp = max(temp, y[j] - x[j])
            ans = max(ans, y[i] + x[i] + temp)

        return ans

    def findMaxValueOfEquationVersion4(self, points: List[List[int]]) -> int:
        """
        y1 - x1, y2 - x2, y3 - x3 的最大值在 i = 4 时算过了, 存在冗余, 用temp记录最大值消除冗余
        时间复杂度 O(n)
        """
        n = len(points)
        x = [0]
        y = [0]
        for point in points:
            x.append(point[0])
            y.append(point[1])
        ans = float("-inf") 
        temp = float("-inf")
        for i in range(2, n+1):
            temp = max(temp, y[i - 1] - x[i - 1])
            ans = max(ans, y[i] + x[i] + temp)

        return ans

class Solution:

    """
    给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。
    请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
    题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。

    思路
        还是设 j < i, 多了个 xi - xj < k -> xj > xi - k
        也就是 j 和 i 离得不能太远
        当 i 增大时, j 的取值范围上下界同时增大, 要维护 yj - xj 的max
        这其实就是滑动窗口, 求最大值
    """
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -1e9
        q = deque()
        n = len(points)
        for i in range(0, n):
            # 维护队头: while x[j] < x[i] - k, 删除过期的j
            while q and points[q[0]][0] < points[i][0] - k:
                q.popleft()
            # 更新答案: ans = max(ans, y[i] + x[i] + y[j] - x[j])
            if q: ans = max(ans, points[i][1] + points[i][0] + points[q[0]][1] - points[q[0]][0])
            # 维护单调性: y[j] - x[j] 单调递减的队列
            while q and points[q[-1]][1] - points[q[-1]][0] <= points[i][1] - points[i][0]:
                q.pop()
            q.append(i)

        print("ans: %s" % ans)
        return ans


class TestFindMaxValueWithoutK:

    """
    pytest -s 1499_max_value_of_equation.py::TestFindMaxValueWithoutK::test1
    pytest -s 1499_max_value_of_equation.py::TestFindMaxValueWithoutK::test2
    pytest -s 1499_max_value_of_equation.py::TestFindMaxValueWithoutK::test3
    pytest -s 1499_max_value_of_equation.py::TestFindMaxValueWithoutK::test4
    """

    def test1(self):
        solution = Solution1()

        points = [[1,3],[2,0],[5,10],[6,-10]]
        assert 17 == solution.findMaxValueOfEquationVersion1(points)

        points = [[0,0],[3,0],[9,2]]
        assert 11 == solution.findMaxValueOfEquationVersion1(points)
    
    def test2(self):
        solution = Solution1()

        points = [[1,3],[2,0],[5,10],[6,-10]]
        assert 17 == solution.findMaxValueOfEquationVersion2(points)

        points = [[0,0],[3,0],[9,2]]
        assert 11 == solution.findMaxValueOfEquationVersion2(points)
    
    def test3(self):
        solution = Solution1()

        points = [[1,3],[2,0],[5,10],[6,-10]]
        assert 17 == solution.findMaxValueOfEquationVersion3(points)

        points = [[0,0],[3,0],[9,2]]
        assert 11 == solution.findMaxValueOfEquationVersion3(points)
    
    def test4(self):
        solution = Solution1()

        points = [[1,3],[2,0],[5,10],[6,-10]]
        assert 17 == solution.findMaxValueOfEquationVersion4(points)

        points = [[0,0],[3,0],[9,2]]
        assert 11 == solution.findMaxValueOfEquationVersion4(points)


class TestFindMaxValue:

    """
    pytest -s 1499_max_value_of_equation.py::TestFindMaxValue
    """

    def test(self):
        solution = Solution()

        """
        前两个点满足 |xi - xj| <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
        没有其他满足条件的点，所以返回 4 和 1 中最大的那个。
        """
        points = [[1,3],[2,0],[5,10],[6,-10]]; k = 1
        assert 4 == solution.findMaxValueOfEquation(points, k)

        points = [[0,0],[3,0],[9,2]]; k = 3
        assert 3 == solution.findMaxValueOfEquation(points, k)
