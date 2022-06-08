# -*- coding:utf-8 -*-


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == -(1 << 31):
            return 1.0 / (self.myPow(x, -(n + 1))) * x
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        
        temp = self.myPow(x, n // 2)
        # 偶数次幂, ans = temp * temp, 奇数次幂, 要乘多 1 次 x
        if n % 2 == 0:
            ans = temp * temp
        else:
            ans = temp * temp * x
        return ans
    
    def myPow2(self, x: float, n: int) -> float:
        """[幂乘，迭代法，二进制移位法]

        时间复杂度为: o(log n), 递归的层数
        空间复杂度为 o(1), 没有用到额外的空间，故为O(1)


        Args:
            x (float): [description]
            n (int): [description]

        Returns:
            float: [description]
        """
        # 当 x = 0.0x=0.0 时：直接返回 0.00.0 ，以避免后续 11 除以 00 操作报错。分析： 数字 00 的正数次幂恒为 00 ； 00 的 00 次幂和负数次幂没有意义，因此直接返回 0.00.0 即可。
        if x == 0.0:
            return 0.0
        # 初始化结果为1
        res = 1
        # 当 n < 0 时，把问题转化至 n >= 0 范围内, 即执行 x = 1 / x, n = -n
        if n <0:
            x, n = 1 / x, -n
        
        # n = 0 跳出循环
        while n:
            # n & 1 为 True 的话，证明是奇数，奇数的话，需要补乘 x
            if n & 1:
                res *= x
            # 执行 x = x * x
            x *= x
            # 执行 n 右移 一位
            n >>= 1
        
        return res


class TestMyPow:

    """
    pytest -s 50_pow.py::TestMyPow
    """

    def test(self):

        solution = Solution()

        x, n = 2.00000, 10
        assert 1024.00000 == solution.myPow(x, n)

        x, n = 2.10000, 3
        assert 9.26100 == round(solution.myPow(x, n), 3)

        x, n = 2.00000, -2
        assert 0.25000 == solution.myPow(x, n)

