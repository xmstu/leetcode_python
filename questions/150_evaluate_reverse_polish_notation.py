# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """后缀表达式运算"""
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                y = stack.pop()
                x = stack.pop()
                res = self.calc(x, y, token)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]
    
    def calc(self, x: int, y: int, token: str):
        if token == "+": return x + y
        if token == "-": return x - y
        if token == "*": return x * y
        if token == "/": return int(x / y)
        return 0


class TestEvalRPN:
    """
    pytest -s 150_evaluate_reverse_polish_notation.py::TestEvalRPN
    """

    def test(self):
        solution = Solution()

        tokens = ["2","1","+","3","*"]
        assert 9 == solution.evalRPN(tokens)

        tokens = ["4","13","5","/","+"]
        assert 6 == solution.evalRPN(tokens)

        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        assert 22 == solution.evalRPN(tokens)
