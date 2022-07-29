# -*- coding:utf-8 -*-


class Solution:
    """
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

    思路:
        递归, 走两个分支, 删或不删, times控制删的次数
    """
    def validPalindrome(self, s: str) -> bool:
        def check(s: str, l: int, r: int, times: int):
            while l < r:
                # 不相等就选择删左端或右端
                if s[l] != s[r]:
                    return times > 0 and (check(s, l+1, r, times-1) or check(s, l, r-1, times-1)) 
                l += 1
                r -= 1
            return True
        return check(s, 0, len(s) - 1, 1)

class TestIsPalindrome:

	"""
	pytest -s 680_valid_palindrome2.py::TestIsPalindrome
	"""
	def test(self):
		solution = Solution()

		s = "aba"
		assert True == solution.validPalindrome(s)

		s = "abca"
		assert True == solution.validPalindrome(s)

		s = "abc"
		assert False == solution.validPalindrome(s)
