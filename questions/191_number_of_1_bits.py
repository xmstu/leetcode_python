# -*- coding:utf-8 -*-


class Solution:

    """
    编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
    提示：
        请注意，在某些语言, 如 Java中, 没有无符号整数类型。
        在这种情况下, 输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，
        其内部的二进制表示形式都是相同的。
        在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
    """
    def hammingWeight(self, n: int) -> int:
        """
        思路: 每次让 n 和 1 进行 与运算, 最低位是 1, 1的数量数量加1, 是0不加, 每次运算完后右移一位
        """
        cnt = 0
        while n > 0:
            if n & 1 == 1:
                cnt += 1
            n = n >> 1
        return cnt


class Solution2:

    def hammingWeight(self, n: int) -> int:
        """
        思路: 取位运算, 看每一位是否为1, 思想和和方法1差不多, 只不过方法2每次右移 i 位, 且 n 不变
        """
        cnt = 0
        for i in range(32):
            if (n >> i) & 1:
                cnt += 1
        return cnt


class Solution3:

    def hammingWeight(self, n: int) -> int:
        """
        思路: 用lowbit运算, 每次看高位有没有1, 有的数量加1, 然后通过与运算去掉高位的1, 直到数字为0
        """
        cnt = 0
        while n > 0:
            cnt += 1
            n = n & (n - 1)
        
        return cnt


class TestHammingWeight:

    """
    pytest -s 191_number_of_1_bits.py::TestHammingWeight
    """

    def test(self):

        solution = Solution3()

        n = 0b00000000000000000000000000001011
        assert 3 == solution.hammingWeight(n)

        n = 0b00000000000000000000000010000000
        assert 1 == solution.hammingWeight(n)

        n = 0b11111111111111111111111111111101
        assert 31 == solution.hammingWeight(n)






