# -*- coding:utf-8 -*-


class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 1, x
        while left < right:
            mid = (left + right + 1) // 2 
            if mid <= x / mid:
                left = mid
            else:
                right = mid - 1
        
        return right
    
    def myRealSqrt(self, x: float):
        left, right = 0.0, x
        # 精确到小数点后7位
        # 实数二分得到的是一个点, 就不用考虑 加一或减一 的问题
        while (right - left) > 1e-7:
            mid = (left + right) / 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid
        
        print("right: %s, left: %s" % (right, left))
        return int(right)


class TestMySqrt:

    """
    pytest -s 69_sqrt.py::TestMySqrt
    """

    def test(self):
        solution = Solution()

        assert 2 == solution.mySqrt(4)
        assert 2 == solution.mySqrt(8)
        assert 2 == solution.myRealSqrt(8)
