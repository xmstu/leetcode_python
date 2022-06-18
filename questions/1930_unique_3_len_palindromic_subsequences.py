# -*- coding:utf-8 -*-


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        for c in set(s):
            # 找出当前字符在 s 字符串中 最左位置和最右位置, 两个位置之间有多少个不重复的字符就是有多少个不同的三字回文串
            left=s.index(c)
            right=s.rindex(c)
            ans+=len(set(s[left+1:right]))
        return ans


class TestCountPalindromicSubsequences:

    """
    pytest -s 1930_unique_3_len_palindromic_subsequences.py::TestCountPalindromicSubsequences
    """

    def test(self):
        solution = Solution()

        s = "aabca"
        assert 3 == solution.countPalindromicSubsequence(s)

        s = "adc"
        assert 0 == solution.countPalindromicSubsequence(s)

        s = "bbcbaba"
        assert 4 == solution.countPalindromicSubsequence(s)
