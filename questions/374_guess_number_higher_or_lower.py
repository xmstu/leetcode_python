# -*- coding:utf-8 -*-

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


pick = None

def guess(num: int):
    if pick == num:
        return 0
    elif pick < num:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1

class TestGuessNumber:

    """
    pytest -s 374_guess_number_higher_or_lower.py::TestGuessNumber
    """

    def test(self):
        solution = Solution()

        global pick

        pick = 1000000
        assert 1000000 == solution.guessNumber(2 ** 31)

        pick = 1
        assert 1 == solution.guessNumber(1)
