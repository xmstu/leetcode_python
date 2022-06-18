# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        顺时针旋转矩阵 90 度
        使用辅助数组
        """
        nrow, ncol = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(ncol)] for _ in range(nrow)]
        for row in range(nrow):
            for col in range(ncol):
                new_matrix[col][ncol - 1 - row] = matrix[row][col]
        print("new_matrix: %s" % new_matrix)
        matrix[:] = new_matrix
    
    def rotateInPlace(self, matrix: List[List[int]]) -> None:
        """
        原地旋转
        """
        # 按照对角线翻转后
        nrow, ncol = len(matrix), len(matrix[0])
        for row in range(nrow):
            for col in range(row, ncol):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # 再每层反转列表
        for row_list in matrix:
            i, j = 0, len(row_list) - 1
            while i < j:
                row_list[i], row_list[j] = row_list[j], row_list[i]
                i += 1
                j -= 1
    
    def rotateReverseInPlace(self, matrix: List[List[int]]) -> None:
        """
        原地旋转回来
        """
        # 再每层反转列表
        for row_list in matrix:
            i, j = 0, len(row_list) - 1
            while i < j:
                row_list[i], row_list[j] = row_list[j], row_list[i]
                i += 1
                j -= 1
        # 按照对角线翻转后
        nrow, ncol = len(matrix), len(matrix[0])
        for row in range(nrow):
            for col in range(row, ncol):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        print("reverse matrix: %s" % matrix)


class TestRotate:

    """
    pytest -s rotate_matrix.py::TestRotate
    """

    def test(self):
        solution = Solution()


        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]
        matrix1 = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]
        expect_matrix = [
            [7,4,1],
            [8,5,2],
            [9,6,3],
        ]
        solution.rotateInPlace(matrix)
        assert expect_matrix == matrix

        solution.rotateReverseInPlace(matrix)
        assert matrix1 == matrix
