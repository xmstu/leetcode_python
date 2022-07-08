# -*- coding:utf-8 -*-


class Solution:
    """
    给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
    一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
    两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # 处理动规边界问题, 从下标1开始遍历, 避免边界判断
        text1 = " " + text1
        text2 = " " + text2
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i] == text2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        
        return f[m][n]


class TestLCS:

    """
    pytest -s 1143_longest_common_subsequence.py::TestLCS
    """

    def test(self):
        solution = Solution()

        text1 = "abcde"; text2 = "ace" 
        assert 3 == solution.longestCommonSubsequence(text1, text2)

        text1 = "abc"; text2 = "abc"
        assert 3 == solution.longestCommonSubsequence(text1, text2)

        text1 = "abc"; text2 = "def"
        assert 0 == solution.longestCommonSubsequence(text1, text2)
