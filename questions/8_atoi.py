# -*- coding:utf-8 -*-


class Solution:
    """
    请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

    函数 myAtoi(string s) 的算法如下：

    读入字符串并丢弃无用的前导空格
    检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
    读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
    返回整数作为最终结果。
    注意：

    本题中的空白字符只包括空格字符 ' ' 。
    除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
    """
    def myAtoi(self, s: str) -> int:
        index = 0
        n = len(s)
        # 1. 忽略前导空格
        while index < n and s[index] == ' ':
            index += 1

        # 2. 处理正负号
        sign = 1
        if index < n and s[index] in ("+", "-"):
            sign = 1 if s[index] == "+" else -1
            index += 1
        # 3. 处理数字直到非数字或结尾
        val = 0
        while index < n and '0' <= s[index] <= '9':
            # 判断数字有无溢出
            if val > (2147483647 - (int(s[index]) - 0)) / 10:
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
            val = val * 10 + (int(s[index]) - 0)
            index += 1


        return sign * val


class TestMyAtoi:

    """
    pytest -s 8_atoi.py::TestMyAtoi
    """

    def test(self):
        solution = Solution()

        s = "42"
        assert 42 == solution.myAtoi(s)

        s = "   -42"
        assert -42 == solution.myAtoi(s)

        s = "4193 with words"
        assert 4193 == solution.myAtoi(s)
