# -*- coding:utf-8 -*-


class Solution:
    """
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

    思路:
        f[i][j] 表示 s 的前 i 个字符, p的前j个字符, 能否匹配
        如果 p[j] 是 a~z, f[i][j] = f[i-1][j-1] && s[i] == p[j]
        如果 p[j] 是 . , f[i][j] = f[i-1][j-1]
        如果是 p[j] 是 *
            (1) 继续配 (s[i] 被 * 包含) f[i][j] <- f[i-1][j] && (s[i]==p[j-1] || p[j-1]=='.')
                a. s = 'aa' 和 p = 'a*'
                b. s = 'ab' 和 p = '.*' 
            (2) 停止匹配(* 的使命完成) f[i][j] = f[i][j-2]
        
        初值: f[0][0] = True, f[0][j] = True (s = "aab", p = "c*a*b")
        目标: f[n][m]
    """
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        s = " " + s
        p = " " + p

        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for j in range(2, m+1, 2):
            if p[j] == "*":
                f[0][j] = True
            else:
                break
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if 'a' <= p[j] <= 'z':
                    f[i][j] = f[i-1][j-1] and s[i] == p[j]
                elif p[j] == '.':
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = f[i][j-2]
                    if s[i] == p[j-1] or p[j-1] == '.':
                        f[i][j] = f[i][j] or f[i-1][j]

        return f[n][m]


class TestIsMatch:

    """
    pytest -s 10_regular_exp_match.py::TestIsMatch
    """

    def test(self):
        solution = Solution()

        s = "aa"; p = "a"
        assert False == solution.isMatch(s, p)

        s = "aa"; p = "a*"
        assert True == solution.isMatch(s, p)

        s = "ab"; p = ".*"
        assert True == solution.isMatch(s, p)


