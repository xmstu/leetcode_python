# -*- coding:utf-8 -*-


class Solution:
    """
    给你一个字符串 s，找到 s 中最长的回文子串。
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        anslen = 0
        ansStart = 0
        # 奇回文串
        for centre in range(0, n):
            l = centre - 1
            r = centre + 1
            # 以 centre 为中心, 向左右扩展
            while l >= 0 and r < n  and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > anslen:
                anslen = r - l - 1
                ansStart = l + 1
        # 偶回文串
        for centre in range(1, n):
            l = centre - 1
            r = centre
            # 以 centre 为中心, 向左右扩展
            while l >= 0 and r < n  and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > anslen:
                anslen = r - l - 1
                ansStart = l + 1

        return s[ansStart:ansStart+anslen]


class Solution2:
    """
    给你一个字符串 s，找到 s 中最长的回文子串。
    思路: 前后缀hash + 二分答案 获取最长回文子串
    """
    def longestPalindrome(self, s: str) -> str:
        b = 131
        p = int(1e9 + 7)
        n = len(s)
        preH = [0] * (n+1)
        sufH = [0] * (n+2)
        powB = [0] * (n+1)
        powB[0] = 1

        # 计算前缀 hash 
        for i in range(1, n+1):
            preH[i] = (preH[i-1] * b + (ord(s[i-1]) - ord('a') + 1)) % p
            powB[i] = powB[i-1] * b % p
        
        # 计算后缀 hash
        for i in range(n, 0, -1):
            sufH[i] = (sufH[i+1] * b + (ord(s[i-1]) - ord('a') + 1)) % p
        
        def calcHash(l: int, r: int):
            """
            s = "foobar"
            fooba - fo000 = oba
            """
            return ((preH[r+1] - preH[l] * powB[r-l+1]) % p + p) % p 
        
        def calcReverseHash(l: int, r: int):
            """
            s = "foobar"
            raboo - r000 = abo
            """
            return ((sufH[l+1] - sufH[r+2] * powB[r-l+1]) % p + p) % p 


        anslen = 0
        ansStart = 0
        # 奇回文串
        for centre in range(0, n):
            # 二分求从 centre 往两侧可以扩展多少字符
            left = 0
            right = min(centre, n - 1 - centre)
            while left < right:
                mid = (left + right + 1) // 2
                if calcHash(centre - mid, centre + mid) == calcReverseHash(centre - mid, centre + mid):
                    left = mid
                else:
                    right = mid - 1
                
            if 2 * right + 1 > anslen:
                anslen = 2 * right + 1
                ansStart = centre - right

        # 偶回文串
        for centre in range(1, n):
            # 二分求从 centre-1和centre 往两侧可以扩展多少字符
            left = -1
            right = min(centre-1, n - 1 - centre)
            while left < right:
                mid = (left + right + 1) // 2
                if calcHash(centre - 1 - mid, centre + mid) == calcReverseHash(centre - 1 - mid, centre + mid):
                    left = mid
                else:
                    right = mid - 1
                
            if 2 * right + 2 > anslen:
                anslen = 2 * right + 2
                ansStart = centre - 1 - right
        
        return s[ansStart:ansStart+anslen]
    


class TestLongestPalindrome:

    """
    pytest -s 5_longest_palindromic_substr.py::TestLongestPalindrome
    """

    def test(self):
        solution = Solution2()

        s = "babad"
        assert "bab" == solution.longestPalindrome(s)

        s = "cbbd"
        assert "bb" == solution.longestPalindrome(s)

