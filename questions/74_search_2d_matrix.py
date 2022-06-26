# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 找到目标行, 再对目标行进行二分
        target_row = None
        for row_list in matrix:
            if row_list[0] <= target <= row_list[-1]:
                target_row = row_list
                break
        if not target_row:
            return False
        
        left, right = 0, len(target_row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target_row[mid] == target:
                return True
            if target_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


class SolutionDirectBinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_row = mid // len(matrix[0])
            mid_col = mid % len(matrix[0])
            if matrix[mid_row][mid_col] == target:
                return True
            if matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


class SolutionCoordinateAxis:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 以左下角作为坐标轴原点, 大于目标值, row -= 1, 小于目标值, col += 1
        if not matrix:
            return False
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False


class TestSearchMatrix:

    """
    pytest -s 74_search_2d_matrix.py::TestSearchMatrix
    """

    def test(self):
        solution = Solution()

        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3
        assert True == solution.searchMatrix(matrix, target)

        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 13
        assert False == solution.searchMatrix(matrix, target)
