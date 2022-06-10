# -*- coding:utf-8 -*-
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 每次从左上角遍历到右下角, 暴力求解, 会超时
        ans = 0
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                ans += self.matrix[r][c]
        return ans
    

class NumMatrixOneDimension:
    """
    一维前缀和
    """

    def __init__(self, matrix: List[List[int]]):
        # 提前算好每个位置的前缀和
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i][j + 1] = _sums[i][j] + matrix[i][j]
                res = _sums[i][j + 1]
                a = _sums[i][j]
                b = matrix[i][j]
                print("_sums[{i}][{j} + 1]: {res} = _sums[{i}][{j}]: {a} + matrx[{i}][{j}]: {b}".format(i=i, j=j, res=res, a=a, b=b))
        print("_sums: %s" % _sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        # 每行计算 前缀和 - col1 对应的数, 就可以得到 row = i, col1 到 col2 的总和
        total = sum(_sums[i][col2 + 1] - _sums[i][col1] for i in range(row1, row2 + 1))
        return total


class NumMatrixTwoDimension:
    """
    二维前缀和
    """

    def __init__(self, matrix: List[List[int]]):
        """
        构造二维前缀和二维数组
        假设:
            A  | X1
            X2 | D
        D 是 (row1,col1) 和 (row2,col2) 括起来的子矩阵
        A 是 (0,0) 和 (row1-1,col1-1) 括起来的子矩阵
        B 是 (0,0) 和 (row1-1,col1) 括起来的面积: B = A + X1
        C 是 (0,0) 和 (row1,col1-1) 括起来的面积: C = A + X2
        S 是 (0,0) 和 (row2, col2) 括起来的子矩阵

        求 D 的面积
            D = S - X1 - X2 - A = S - (X1 + A) - (X2 + A) - A + 2A = S - B - C + A  
        
        转换成公式就是:
            sumRegion(row1, col1, row2, col2) = f(row2, col2) - f(row1 - 1, col2) - f(row2, col1 - 1) + f(row1 - 1, col1 - 1)
            f(row2, col2) = f(row1 - 1, col2) + f(row2, col1 - 1) - f(row1 - 1, col1 - 1) + matrix[i][j]
        为了避免判断 row1 = 0, col1 = 0 的判断, 计算从 (1,1) 开始
        公式转换为:
            sumRegion(row1, col1, row2, col2) = f(row2+1, col2+1) - f(row1, col2+1) - f(row2+1, col1) + f(row1, col1)
        """
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                # f(row2+1, col2+1) = f(row1, col2+1) + f(row2+1, col1) - f(row1, col1) + matrix[i][j]
                _sums[i + 1][j + 1] = _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]
        print("_sums: %s" % _sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums
        # sumRegion(row1, col1, row2, col2) = f(row2+1, col2+1) - f(row1, col2+1) - f(row2+1, col1) + f(row1, col1)
        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]


class TestSumRegion:
    """
    pytest -s 304_range_sum_query_2d_immutable.py::TestSumRegion
    """

    def test(self):
        matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
        obj = NumMatrix(matrix)

        assert 8 == obj.sumRegion(2,1,4,3)
        assert 11 == obj.sumRegion(1,1,2,2)
        assert 12 == obj.sumRegion(1,2,2,4)
        
        obj = NumMatrixOneDimension(matrix)

        assert 8 == obj.sumRegion(2,1,4,3)
        assert 11 == obj.sumRegion(1,1,2,2)
        assert 12 == obj.sumRegion(1,2,2,4)

        obj = NumMatrixTwoDimension(matrix)

        assert 8 == obj.sumRegion(2,1,4,3)
        assert 11 == obj.sumRegion(1,1,2,2)
        assert 12 == obj.sumRegion(1,2,2,4)



