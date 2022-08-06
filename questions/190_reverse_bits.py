# -*- coding:utf-8 -*-


class Solution:
    """
    颠倒给定的 32 位无符号整数的二进制位。

    提示：
        请注意，在某些语言 (如 Java) 中, 没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
        在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在 示例 2 中，输入表示有符号整数 -3, 输出表示有符号整数 -1073741825。
    """
    def reverseBits(self, n: int) -> int:
        """
        思路: 
        1. ans 每次左移1位, n 右移 i 位并和 1 进行运算取得低位, 低位和ans的低位进行 或 运算, 0 或 0 不变, 0 或 1 得到 1
        2. 这样不停循环, 就可以颠倒二进制数
        """
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n >> i & 1)
        
        return ans


class TestReverseBits:

    """
    pytest -s 190_reverse_bits.py::TestReverseBits
    """

    def test(self):
        solution = Solution()

        n = 0b00000010100101000001111010011100
        assert 0b00111001011110000010100101000000 == solution.reverseBits(n)

        n = 0b11111111111111111111111111111101
        assert 0b10111111111111111111111111111111 == solution.reverseBits(n)

