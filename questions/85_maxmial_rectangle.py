# -*- coding:utf-8 -*-
from typing import List


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def __repr__(self) -> str:
        return "(width: %s, height: %s)" % (self.width, self.height)


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        heights = [0] * len(matrix[0])
        maxArea = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        ans = 0
        # 补一个0, 可以将有效的柱子全部弹空, 并且0不影响最终答案
        heights.append(0)
        # 维护一个单调栈, 遇到破坏单调栈的柱子, 就计算当前栈内所有大于当前高度的柱子可向左扩展的面积, 并弹出栈顶, 将宽度贡献给新柱子
        for height in heights:
            accumulateWidth = 0
            # 栈顶的柱子高度大于等于新的柱子的高度, 单调递增的特性破坏了, 计算栈内所有大于当前高度的柱子可向左扩展的面积
            while s and s[-1].height >= height:
                # 将宽度贡献给新的柱子后, 弹出栈顶, 维护单调递增的特性
                accumulateWidth += s[-1].width
                # 更新最大面积
                ans = max(ans, s.pop().height * accumulateWidth)
                print("ans: %s, accumulateWidth: %s" % (ans, accumulateWidth))
            # 将新柱子压入栈
            s.append(Rectangle(accumulateWidth + 1, height))
            print("s: %s" % s)
        
        return ans


class TestMaximalRectangle:

    """
    pytest -s 85_maxmial_rectangle.py::TestMaximalRectangle
    """

    def test(self):
        solution = Solution()

        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        assert 6 == solution.maximalRectangle(matrix)

        matrix = [["0"]]
        assert 0 == solution.maximalRectangle(matrix)

        matrix = [["1"]]
        assert 1 == solution.maximalRectangle(matrix)

