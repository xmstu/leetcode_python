# -*- coding:utf-8 -*-


class Solution:
    """
    给你一个整数 n, 请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
    如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
    """
    def isPowerOfTwo(self, n: int) -> bool:
        """
        思路: 一位位左移, 判断 res 是否 大于 n, 大于返回 False, 等于返回 True, 小于继续循环
        """ 
        for i in range(32):
            res = 1 << i
            if res > n:
                return False
            elif res == n:
                return True
            else:
                continue


class Solution2:
    """
    给你一个整数 n, 请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
    如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
    """
    def isPowerOfTwo(self, n: int) -> bool:
        """
        思路: 用lowbit运算
            1. 负数在二进制中以补码的形式存在, 7 的二进制是 0b0111, 负数是每位取反再加1就是 0b1000 + 0b001 = 0b1001;
            2. 因此, 7 & -7 -> 0b0111 & 0b1001 = 0b0001;
            3. 类似的, 8 的二进制是0b1000, 负数是 0b0111 + 0b0001 = 0b1000, 因此 8 的二进制 正数 和 负数的表示是一样的, 8 & -8 = 8;
        """
        return n > 0 and (n & -n) == n
            

class Solution3:
    """
    给你一个整数 n, 请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
    如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
    """
    def isPowerOfTwo(self, n: int) -> bool:
        """
        思路: 也是 lowbit 运算
            1. 8 & (8-1-7) -> 0b1000 & 0b0111 = 0b0000 == 0;
            1. 7 & (7-1=6) -> 0b0111 & 0b0110 = 0b0110 != 0;
        """
        return n > 0 and n & (n-1) == 0


class TestPowerOfTwo:

    """
    pytest -s 231_power_of_two.py::TestPowerOfTwo
    """

    def test(self):
        solution = Solution3()

        n = 1
        assert True == solution.isPowerOfTwo(n)

        n = 16
        assert True == solution.isPowerOfTwo(n)

        n = 3
        assert False == solution.isPowerOfTwo(n)

        n = 4
        assert True == solution.isPowerOfTwo(n)

        n = 5
        assert False == solution.isPowerOfTwo(n)
