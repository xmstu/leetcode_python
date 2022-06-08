# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def calculate2(self, s: str) -> int:
        """
        由于乘除优先于加减计算，因此不妨考虑先进行所有乘除运算，并将这些乘除运算后的整数值放回原表达式的相应位置，则随后整个表达式的值，就等于一系列整数加减后的值。

        基于此，我们可以用一个栈，保存这些（进行乘除运算后的）整数的值。对于加减号后的数字，将其直接压入栈中；对于乘除号后的数字，可以直接与栈顶元素计算，并替换栈顶元素为计算后的结果。

        具体来说，遍历字符串 s, 并用变量 preSign 记录每个数字之前的运算符，对于第一个数字，其之前的运算符视为加号。每次遍历到数字末尾时，根据 preSign 来决定计算方式：

        加号：将数字压入栈；
        减号：将数字的相反数压入栈；
        乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。
        代码实现中，若读到一个运算符，或者遍历到字符串末尾，即认为是遍历到了数字末尾。处理完该数字后，更新 preSign 为当前遍历的字符。

        遍历完字符串 s 后，将栈中元素累加，即为该字符串表达式的值。
        """
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                print("fuck num: %s" % num)
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
            print("fuck stack: %s" % stack)
        return sum(stack)

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
        for ch in s:
            if '0' <= ch <= '9':
                number += ch
                continue
            else:
                if number:
                    tokens.append(number)
                    number = ""
            if ch == " ":
                continue
            currRank = self.getRank(ch)
            while ops and self.getRank(ops[-1]) >= currRank:
                tokens.append(ops.pop())
            
            ops.append(ch)
        
        while ops:
            tokens.append(ops.pop())

        # 最终中缀表达式转为后缀表达式, 扔给后缀表达式的函数进行计算
        # print("tokens: %s" % tokens)
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


class TestCalculator2:
    """
    pytest -s 227_basic_calculator_2.py::TestCalculator2
    """

    def test(self):
        solution = Solution()

        s = "3+2*2"
        assert 7 == solution.calculate(s)

        s = " 3/2 "
        assert 1 == solution.calculate(s)

        s = " 3+5 / 2 "
        assert 5 == solution.calculate(s)

        s = " 1-1+1"
        assert 1 == solution.calculate(s)

        s = "32+2*2"
        assert 36 == solution.calculate2(s)

        s = " 32/2 "
        assert 16 == solution.calculate2(s)

        s = " 3-6 / 2 "
        assert 0 == solution.calculate2(s)

        s = " 9-1+2"
        assert 10 == solution.calculate2(s)
