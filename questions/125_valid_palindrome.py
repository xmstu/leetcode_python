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


class Solution2:
    def isPalindrome(self, s: str) -> bool:

        def isDigitOrLetter(ch: str):
            return '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
        
        def getNext(s: str, i: int):
            while i < len(s) and not isDigitOrLetter(s[i]):
                i += 1
            return i
        
        def getPre(s: str, i: int):
            while i > 0 and not isDigitOrLetter(s[i]):
                i -= 1
            return i

        def equalsIgnoreCase(ch1: str, ch2: str):
            def lower(ch: str):
                if 'A' <= ch <= 'Z':
                    ch = ord(ch) - ord("A") + ord("a")
                    ch = chr(ch)
                return ch
            return lower(ch1) == lower(ch2)
        
        l = getNext(s, 0)
        r = getPre(s, len(s) - 1)
        while l < r:
            if not equalsIgnoreCase(s[l], s[r]):
                return False
            l = getNext(s, l + 1)
            r = getPre(s, r - 1)
        
        return True



class TestIsPalindrome:

	"""
	pytest -s 125_valid_palindrome.py::TestIsPalindrome
	"""
	def test(self):
		solution = Solution2()

		s = "A man, a plan, a canal: Panama"
		assert True == solution.isPalindrome(s)

		s = "race a car"
		assert False == solution.isPalindrome(s)

		s = " "
		assert True == solution.isPalindrome(s)
