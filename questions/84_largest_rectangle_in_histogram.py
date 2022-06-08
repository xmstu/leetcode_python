# -*- coding:utf-8 -*-
from typing import List


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def __repr__(self) -> str:
        return "(width: %s, height: %s)" % (self.width, self.height)


class Solution:
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
    
    def largestRectangleArea2(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                print("cur_height: %s, cur_width: %s, i: %s, stack[-1]: %s" % (cur_height, cur_width, i, stack[-1]))
                res = max(res, cur_height * cur_width)
            stack.append(i)
            print("stack: %s" % stack)
        return res


class TestLargestRectangleArea:

    """
    pytest -s 84_largest_rectangle_in_histogram.py::TestLargestRectangleArea
    """

    def test(self):
        solution = Solution()

        heights = [2,1,5,6,2,3]
        assert 10 == solution.largestRectangleArea(heights)

        heights = [2,1,5,6,2,3]
        assert 10 == solution.largestRectangleArea2(heights)

        heights = [2,4]
        assert 4 == solution.largestRectangleArea(heights)
