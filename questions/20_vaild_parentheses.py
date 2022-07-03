# -*- coding:utf-8 -*-


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # 左的符号都塞到栈里
            if char in ("(", "[", "{"):
                stack.append(char)
            else:
                # 遇到右的符号, 先判断栈是否为空, 如果为空, 就返回 False
                # 不为空, 就判断栈顶和右符号是否匹配, 不匹配返回false, 匹配就弹出栈顶
                if not stack:
                    return False
                if char == ")" and stack.queue[-1] != '(':
                    return False
                if char == "]" and stack.queue[-1] != '[':
                    return False
                if char == "}" and stack.queue[-1] != '{':
                    return False
                stack.pop()
        # 最后栈为空, 就说明所有符号都是一一对应的, 说明括号有效
        return not stack


class TestParenthesesIsValid:
    """
    pytest -s 20_valid_parentheses.py::TestParenthesesIsValid
    """

    def test(self):
        solution = Solution()

        s = "([])"
        assert True == solution.isValid(s)

        s = "()[]{}"
        assert True == solution.isValid(s)

        s = ")()"
        assert False == solution.isValid(s)

        s = "(((()))"
        assert False == solution.isValid(s)

