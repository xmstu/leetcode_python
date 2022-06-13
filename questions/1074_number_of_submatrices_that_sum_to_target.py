# -*- coding:utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        nr, nc = len(matrix), len(matrix[0])
        pre = [[0] * (nc + 1) for _ in range(nr + 1)]

        for i in range(nr):
            for j in range(nc):
                pre[i+1][j+1] = pre[i][j+1] + pre[i+1][j] - pre[i][j] + matrix[i][j]
        ans = 0
        for i in range(nr + 1):
            for k in range(i + 1, nr + 1):
                dic = defaultdict(int)
                for j in range(nc):
                    tmp = pre[k][nc] - pre[k][j] - pre[i][nc] + pre[i][j]
                    ans += dic[tmp]
                    dic[tmp - target] += 1
                    if tmp == target:
                        ans += 1
        return ans


class TestNumSubmatrixSumTarget:

    """
    pytest -s 1074_number_of_submatrices_that_sum_to_target.py::TestNumSubmatrixSumTarget
    """

    def test(self):
        solution = Solution()

        matrix = [[0,1,0],[1,1,1],[0,1,0]]
        target = 0
        assert 4 == solution.numSubmatrixSumTarget(matrix, target)

        matrix = [[1,-1],[-1,1]]
        target = 0
        assert 5 == solution.numSubmatrixSumTarget(matrix, target)

        matrix = [[904]]
        target = 0
        assert 0 == solution.numSubmatrixSumTarget(matrix, target)


