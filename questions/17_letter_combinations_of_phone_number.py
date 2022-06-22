# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.number_letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.ans = []
        self.chosen = []
        self.recur(digits, 0)
    
        return self.ans
    
    def recur(self, digits: str, i: int):
        # 递归终止条件
        if len(digits) == 0:
            return
        if len(digits) == i:
            self.ans.append("".join(self.chosen))
            return

        # 每层要做的事
        letters = self.number_letter_map[digits[i]]
        for letter in letters:
            self.chosen.append(letter)
            self.recur(digits, i + 1)
            # 回溯, 返回上一层
            self.chosen.pop()


class TestLetterCombinations:

    """
    pytest -s 17_letter_combinations_of_phone_number.py::TestLetterCombinations
    """

    def test(self):
        solution = Solution()

        digits = "23"
        assert ["ad","ae","af","bd","be","bf","cd","ce","cf"] == solution.letterCombinations(digits)

        digits = ""
        assert [] == solution.letterCombinations(digits)

        digits = "2"
        assert ["a", "b", "c"] == solution.letterCombinations(digits)
