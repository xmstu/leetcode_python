# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def calculate2(self, s: str) -> int:
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret

    def calculate(self, s: str) -> int:
        """
        将 s 的表达式, 按照数字 和 运算符分开来, 根据运算符的等级, 构建后缀表达式 tokens
        """
        s += " "
        # 运算符栈
        ops = []
        # 后缀表达式数组
        tokens = []
        # 连续的数字
        number = ""
        # 判断是否需要补0的标志位
        needsZero = True
        for ch in s:
            if '0' <= ch <= '9':
                number += ch
                needsZero = False
                continue
            else:
                if number:
                    tokens.append(number)
                    number = ""
            if ch == " ":
                continue
            if ch == "(":
                ops.append(ch)
                needsZero = True
                continue
            if ch == ")":
                while ops[-1] != "(":
                    tokens.append(ops.pop())
                ops.pop()
                needsZero = False
                continue
            
            if ch in "+-" and needsZero:
                tokens.append("0")

            currRank = self.getRank(ch)
            while ops and self.getRank(ops[-1]) >= currRank:
                tokens.append(ops.pop())
            
            ops.append(ch)
            needsZero = True
        
        while ops:
            tokens.append(ops.pop())

        # 最终中缀表达式转为后缀表达式, 扔给后缀表达式的函数进行计算
        return self.evalRPN(tokens)
    
    def getRank(self, ch: str):
        if ch in ("*", "/"): return 2
        if ch in ("+", "-"): return 1
        return 0

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


class TestCalculator:
    """
    pytest -s 224_basic_calculator.py::TestCalculator
    """

    def test(self):
        solution = Solution()

        s = "1 + 1"
        assert 2 == solution.calculate(s)

        s = "2-1 + 2 "
        assert 3 == solution.calculate(s)

        s = "(1+(4+5+2)-3)+(6+8)"
        assert 23 == solution.calculate(s)

        s = "-(3-1)"
        assert -2 == solution.calculate(s)

        s = "-2 + (4 / 2)"
        assert 0 == solution.calculate(s)

