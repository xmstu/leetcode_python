# -*- coding:utf-8 -*-


class Solution:
    """
    给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
    子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


class TestLongestPalindrome:

    """
    pytest -s 516_longest_palindromic_subsequence.py::TestLongestPalindrome
    """

    def test(self):
        solution = Solution()

        s = "bbbab"
        assert 4 == solution.longestPalindromeSubseq(s)

        s = "cbbd"
        assert 2 == solution.longestPalindromeSubseq(s)
