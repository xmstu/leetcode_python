# -*- coding:utf-8 -*-


class Solution:
    """
    实现 strStr()函数。
    给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

    说明：
    当 needle 是空字符串时, 我们应当返回什么值呢? 这是一个在面试中很好的问题。
    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

    Rabin-Karp 算法
    选用的hash函数:
    把字符串看作一个 b 进制数(一个多项式), 计算它在十进制下对 p 取模的值

    举例:
    取 b = 131, p = 2^64
    字符串 foobar 的 hash 值为 (a=1, b=2, f=6, o=15, r=18)
        (6 * 131^5 + 15 * 131^4 + 15 * 131^3 + 2 * 131^2 + 1 * 131 + 18) mod 2^64
    
    选取的 b 和 p 的值决定了 hash 函数的质量
    根据经验, b = 131, 13331 等, p 为大质数, 冲突概率极小
    hash 值相等时可以在比对一下两个字符串, 避免 hash 碰撞问题

    如何快速计算一个子串的 hash 值
    先计算 6 个前缀子串的 hash 值, O(n)
        H[i] = Hash(s[0...i-1]) = (H[i-1] * b + s[i-1]) mod p
    
    计算子串 oba 的 hash 值
    想当于 b 进制下两个数做减法 (H[5] - H[2] * b^3)
        fooba - fo000 = oba
    Hash(s[l...r]) = (H[r+1] - H[l] * b ^ (r-l+1)) mod p
    """
    def strStr(self, haystack: str, needle: str) -> int:
        b = 131
        p = int(1e9 + 7)
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        haystack = " " + haystack
        needle = " " + needle
       
        # 计算 needle 的 hash 值
        Hneedle = 0
        for i in range(1, m+1):
            Hneedle = (Hneedle * b + (ord(needle[i]) - ord('a') + 1)) % p
        
        # 计算前缀 hash 数组
        H = [0] * (n+1)
        # 计算对应 r-l+1 的次幂
        p131 = [1] * (n+1)
        # a = 1,b = 2, z = 26
        for i in range(1, n+1):
            H[i] = (H[i-1] * b + ord(haystack[i]) - ord('a') + 1) % p
            p131[i] = p131[i-1] * b % p

        print(f"p131: {p131}") 
        for i in range(m, n+1):
            # 判断 s[l~r] 的hash 值 == needle 的 hash值
            if self.calcHash(H, p131, p, i-m+1, i) == Hneedle:
                return i - m

        return -1
    
    def calcHash(self, H, p131, p, l, r):
        hash_value = ((H[r] - H[l-1] * p131[r-l+1]) % p + p) % p
        # print(f"hash_value: {hash_value}")
        return hash_value


class TestStrStr:

    """
    pytest -s 28_implement_strStr.py::TestStrStr
    """
    
    def test(self):
        solution = Solution()

        haystack = "hello"; needle = "ll"
        assert 2 == solution.strStr(haystack, needle)

        haystack = "aaaaa"; needle = "bba"
        assert -1 == solution.strStr(haystack, needle)
