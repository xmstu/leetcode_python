# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        # 初始化增加值为1
        inc = 1
        while i >= 0:
            # 如果数字为9, 需要进位, inc = 1
            if digits[i] == 9:
                digits[i] = 0
            # 如果数字不为9, +1 即可, inc = 0
            else:
                digits[i] = digits[i] + inc
                inc = 0
                break
            
            i -= 1
        
        # 全为 9 的, 需要补一个高位 1
        if inc == 1:
            digits.insert(0, 1)
        
        return digits



class TestPlusOne:
    """
    pytest -s 66_plus_one.py::TestPlusOne
    """

    def test(self):
        solution = Solution()

        nums = [1,2,3]
        assert [1,2,4] == solution.plusOne(nums)

        nums = [1,9,9]
        assert [2,0,0] == solution.plusOne(nums)

        nums = [9,9,9]
        assert [1,0,0,0] == solution.plusOne(nums)

        nums = [9]
        assert [1,0] == solution.plusOne(nums)

        nums = [0]
        assert [1] == solution.plusOne(nums)
