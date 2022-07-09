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


class Solution2:
    """
    给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
    一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
    两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        记录最长公共子序列
        """
        m = len(text1)
        n = len(text2)

        # 处理动规边界问题, 从下标1开始遍历, 避免边界判断
        text1 = " " + text1
        text2 = " " + text2
        f = [[0] * (n + 1) for _ in range(m + 1)]
        # 0 代表是从上一行同一列转移下来, 1 代表是 同一行左一列转移, 2 代表是从对角线上方转移过来
        preType = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i] == text2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    preType[i][j] = 2
                else:
                    if f[i - 1][j] > f[i][j - 1]:
                        f[i][j] = f[i - 1][j]
                        preType[i][j] = 0
                    else:
                        f[i][j] = f[i][j - 1]
                        preType[i][j] = 1
        self.lcs = []
        self.get_lcs(text1, preType, m, n)
        print("self.lcs: %s" % self.lcs)
        return f[m][n]
    
    def get_lcs(self, text1, preType, i, j):
        if i == 0 or j == 0:
            return
        if preType[i][j] == 0:
            self.get_lcs(text1, preType, i - 1, j)
        elif preType[i][j] == 1:
            self.get_lcs(text1, preType, i, j - 1)
        else:
            self.get_lcs(text1, preType, i - 1, j - 1)
            self.lcs.append(text1[i])


class TestLCS:

    """
    pytest -s 1143_longest_common_subsequence.py::TestLCS
    """

    def test(self):
        solution = Solution2()

        text1 = "abcde"; text2 = "ace" 
        assert 3 == solution.longestCommonSubsequence(text1, text2)

        text1 = "abc"; text2 = "abc"
        assert 3 == solution.longestCommonSubsequence(text1, text2)

        text1 = "abc"; text2 = "def"
        assert 0 == solution.longestCommonSubsequence(text1, text2)
