# -*- coding:utf-8 -*-


class Solution:
    """
    给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
    完全平方数 是一个整数, 其值等于另一个整数的平方: 换句话说, 其值等于一个整数自乘的积。例如: 1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

    转移方程: f[i] = 1 + min(f[i - j ** 2]) # (j = 1, j * j <= i)
    """
    def numSquares(self, n: int) -> int:

        f = [0] * (n + 1)
        for i in range(1, n+1):
            minn = 1e9
            j = 1
            while j * j <= i:
                minn = min(minn, f[i - j * j])
                j += 1
            f[i] = minn + 1

        return f[n]


class Solution2:

    def numSquares(self, n: int) -> int:
        square_nums = []
        t = 1
        while t * t <= n:
            square_nums.append(t * t)
            t += 1
        m = len(square_nums)
        f = [[1e9] * (n+1) for _ in range(m+1)]
        f[0][0] = 0


        for i in range(1, m+1):
            x = square_nums[i-1]
            for j in range(0, n+1):
                # 不选 第 i 个数
                f[i][j] = f[i-1][j]
                # 选第 i 个数
                k = 1
                while k * x <= j:
                    if f[i-1][j-k*x] != 1e9:
                        f[i][j] = min(f[i][j], f[i-1][j-k*x] + k)
                    k += 1

        return f[m][n]

class TestNumSquares:

    """
    pytest -s 279_perfect_squares.py::TestNumSquares
    """

    def test(self):
        solution = Solution2()

        """
        12 = 4 + 4 + 4
        """
        n = 12
        assert 3 == solution.numSquares(n)

        n = 13
        assert 2 == solution.numSquares(n)
