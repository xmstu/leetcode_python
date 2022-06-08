# -*- coding:utf-8 -*-
from typing import List


class Rect:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    
    def __repr__(self) -> str:
        return "(width: %s, height: %s)" % (self.width, self.height)


class Solution:
    def trap_dp(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)  # 简化的连续赋值
        # 正向遍历数组 height 得到数组 leftMax 的每个元素值
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        # 反向遍历数组 height 得到数组 rightMax 的每个元素值
        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):  # 逆序遍历
            rightMax[i] = max(rightMax[i + 1], height[i])
        # 遍历每个下标位置即可得到能接的雨水总量
        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

    def trap_double_pointer(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        result = 0
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            print("i: %s, j: %s" % (i, j))
            print("left max: %s, right_max: %s" % (left_max, right_max))
            print("result: %s" % result)
            if left_max < right_max:
                result += left_max - height[i]
                print("result: %s, left max: %s, height[%s]: %s" % (result, left_max, i, height[i]))
                i += 1
            else:
                result += right_max - height[j]
                print("result: %s, right max: %s, height[%s]: %s" % (result, right_max, j, height[j]))
                j -= 1
            print()
        print("final result: %s" % result)
        return result
    
    def trap_stack(self, height: List[int]) -> int:
        ans = 0
        stack = list()  # 用列表来模拟实现栈
        n = len(height)
        
        for i, h in enumerate(height):  # 同时获取下标和对应的高度
            # height[i] > height[stack[-1]]得到一个可以接雨水的区域
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack: # 栈为空,左边不存在最大值,无法接雨水
                    break
                left = stack[-1] # left成为新的栈顶元素
                currWidth = i - left - 1 # 获取接雨水区域的宽度
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i) # 在对下标i处计算能接的雨水量之后,将i入栈,继续遍历后面的下标
        
        return ans
    
    def trap_stack2(self, heights: List[int]) -> int:
        ans = 0 
        stack = [Rect(0, 0)]
        for height in heights:
            accWidth = 0
            # 雨水遇到更高的墙壁, 就破坏了栈的单调递减的特性, 需要计算可以接的雨水和维护栈单调递减的特性
            while len(stack) > 1 and stack[-1].height <= height:
                accWidth += stack[-1].width
                bottom = stack[-1].height
                stack.pop()
                ans += accWidth * max(0, min(stack[-1].height, height) - bottom)
                print("ans: %s, stack[-1]: %s, cur height: %s, bottom: %s, accWidth: %s" % (ans, stack[-1], height, bottom, accWidth))
            stack.append(Rect(height, accWidth + 1))
            print("stack: %s" % stack)
        return ans


class TestCatchRain(object):

    """
    pytest -s 42_catch_rain.py::TestCatchRain
    """

    def test_catch_rain(self):
        solution = Solution()

        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # assert 6 == solution.trap_double_pointer(height)

        # height = [4,2,0,3,2,5]
        # assert 9 == solution.trap_dp(height)

        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        assert 6 == solution.trap_stack2(height)
