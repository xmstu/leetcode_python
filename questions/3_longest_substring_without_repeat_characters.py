# -*- coding:utf-8 -*-


class Solution:
    """
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
    利用滑动窗口，右指针不断往右前进，左指针在子串遇到重复的时候就收缩, 向右前进

    其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
    当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_substr_length = 0
        # 右指针，初始为 -1, 相当于我们在字符串的左边界的左侧，还没有开始移动
        rk = -1
        n = len(s)
        for i in range(n):
            print("i: %s, char set: %s, s[i]: %s" % (i, char_set, s[i]))
            if i != 0:
                # 收缩窗口, 左指针向右移动一格，从 set 中移除一个字符
                char_set.remove(s[i - 1])
                print("remove, char set: %s" % char_set)
            while rk + 1 < n and s[rk + 1] not in char_set:
                # 右指针不断移动
                char_set.add(s[rk + 1])
                rk += 1
            
            max_substr_length = max(max_substr_length, rk - i + 1)
       
        return max_substr_length
    
    def lengthOfLongestSubstringHashMap(self, s: str) -> int:
        max_substr_length = 0
        table = {}
        start = 0
        for end, v in enumerate(s):
            if v in table.key():
                start = max(table.get(v) + 1, start)
            max_substr_length = max(max_substr_length, end - start + 1)
            table[v] = end
            print("table: %s" % table)
        return max_substr_length


class TestlengthOfLongestSubstring(object):
    """
    pytest -s 3_longest_substring_without_repeat_characters.py::TestlengthOfLongestSubstring
    """

    def test_get_longest_substr_length(self):
        solution = Solution()
        s = "abcabcbb"
        assert 3 == solution.lengthOfLongestSubstring(s)
        s = "bbbbb"
        assert 1 == solution.lengthOfLongestSubstring(s)
        s = "pwwkew"
        assert 3 == solution.lengthOfLongestSubstringHashMap(s)
        s = ""
        assert 0 == solution.lengthOfLongestSubstring(s)
        s = " "
        assert 1 == solution.lengthOfLongestSubstring(s)
        s = "aab"
        assert 2 == solution.lengthOfLongestSubstringHashMap(s)
        s = "dvdf"
        assert 3 == solution.lengthOfLongestSubstringHashMap(s)
