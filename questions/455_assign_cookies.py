from typing import List

class Solution:
    """
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
    对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；
    并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
    你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        g[i] <= s[j] 的 i 都可以满足
        g[i1] <= g[i2] <= s[j] 满足 i2 更好, 可以留下更大的饼干去满足胃口更小的孩子
        """
        ans = 0
        g.sort()
        s.sort()
        j = 0
        for child in g:
            while j < len(s) and s[j] < child:
                j += 1
            if j < len(s):
                ans += 1
                j += 1
        return ans


class TestFindContentChildren:

    """
    pytest -s 455_assign_cookies.py::TestFindContentChildren
    """

    def test(self):
        solution = Solution()

        g = [1,2,3]; s = [1,1]
        assert 1 == solution.findContentChildren(g, s)

        g = [1,2]; s = [1,2,3]
        assert 2 == solution.findContentChildren(g, s)
