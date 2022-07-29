# -*- coding:utf-8 -*-


class Solution:

    """
    给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
    字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
    题目数据保证答案符合 32 位带符号整数范围。

    思路:
        f[i][j] 表示 s[1~i] 选子序列得到 t[1~j]的方案数
        f[i][j] = f[i-1][j]
        如果 s[i] == t[j] 有 f[i][j] += f[i-1][j-1]

        初值: f[i][0] = 1
        目标: f[n][m]
    """
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        s = " " + s
        t = " " + t

        f = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            f[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                f[i][j] = f[i-1][j]
                if s[i] == t[j] and f[i][j] <= 2147483647 -  f[i-1][j-1]:
                    f[i][j] += f[i-1][j-1]
        return f[n][m]


class TestNumDistinct:

    """
    pytest -s 115_distinct_subsequences.py::TestNumDistinct
    """

    def test(self):
        solution = Solution()

        s = "rabbbit"; t = "rabbit"
        assert 3 == solution.numDistinct(s, t)

        s = "babgbag"; t = "bag"
        assert 5 == solution.numDistinct(s, t)
