# -*- coding:utf-8 -*-


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        res = True

        def vaildChar(c: str) -> bool:
            return ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")  

        while i < j:
            if not vaildChar(s[i]):
                i += 1
                continue
            if not vaildChar(s[j]):
                j -= 1
                continue
            if s[i] != s[j]:
                res = False
                break
            i += 1
            j -= 1
        
        return res



class TestIsPalindrome:

	"""
	pytest -s 125_valid_palindrome.py::TestIsPalindrome
	"""
	def test(self):
		solution = Solution()

		s = "A man, a plan, a canal: Panama"
		assert True == solution.isPalindrome(s)

		s = "race a car"
		assert False == solution.isPalindrome(s)

		s = " "
		assert True == solution.isPalindrome(s)
