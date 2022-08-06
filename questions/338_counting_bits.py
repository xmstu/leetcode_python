# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
    """
    def countBits(self, n: int) -> List[int]:
        """
        思路: 利用 lowbit 运算, 得到递推式子: cnt[i] = cnt[i & (i-1)] + 1
        """
        cnt = [0] * (n+1)
        for i in range(1, n+1):
            cnt[i] = cnt[i & (i - 1)] + 1
        return cnt


class TestCountBits:

    """
    pytest -s 338_counting_bits.py::TestCountBits
    """

    def test(self):
        solution = Solution()

        n = 2
        assert [0,1,1] == solution.countBits(n)

        n = 5
        assert [0,1,1,2,1,2] == solution.countBits(n)


