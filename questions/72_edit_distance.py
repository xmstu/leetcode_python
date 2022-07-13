# -*- coding:utf-8 -*-


class Solution:
    """
    给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
    你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符
    """
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        word1 = " " + word1
        word2 = " " + word2

        f = [[float("inf")] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j
        
        print("init f: %s" % f)
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                f[i][j] = min(
                    f[i][j - 1] + 1,  # 插入字符
                    f[i - 1][j] + 1,  # 删除字符
                    f[i - 1][j - 1] + (word1[i] != word2[j]),  # 替换字符, 如果一样就不用替换, 不一样编辑距离+1 
                    )
        
        print("dp f: %s" % f)
        return f[n][m]



class TestMinDistance:

    """
    pytest -s 72_edit_distance.py::TestMinDistance
    """

    def test(self):
        solution = Solution()

        """
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')
        """
        word1 = "horse"; word2 = "ros"
        assert 3 == solution.minDistance(word1, word2)

        """
        intention -> inention (删除 't')
        inention -> enention (将 'i' 替换为 'e')
        enention -> exention (将 'n' 替换为 'x')
        exention -> exection (将 'n' 替换为 'c')
        exection -> execution (插入 'u')
        """
        word1 = "intention"; word2 = "execution"
        # assert 5 == solution.minDistance(word1, word2)
