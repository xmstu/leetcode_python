# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    这里有 n 个航班, 它们分别从 1 到 n 进行编号。
    有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
    请你返回一个长度为 n 的数组 answer, 里面的元素是每个航班预定的座位总数。

    思路:
        利用数组的差分获得差分数组, 然后再求差分数组的前缀和, 即可得到对应的座位总数

    航班: 
         1   2   3   4   5
        10     -10
            20     -20
            25             -25
diff:   10  45 -10 -20   0
preSum: 10  55  45  25  25
    """
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # delta 差分数组, 0 和 n + 1 的位置是多余的, 避免if判断
        delta = [0] * (n+2)
        for booking in bookings:
            first, last, seats = booking
            delta[first] += seats
            delta[last+1] -= seats
        
        # 求前缀和
        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + delta[i]

        print(f"preSum: {preSum}")
        # 前缀和数组是从 1 到 n, 因此 0 位置舍去
        return preSum[1:]        


class TestCorpFlightBookings:

    """
    pytest -s 1109_corporate_flight_bookings.py::TestCorpFlightBookings
    """

    def test(self):
        solution = Solution()

        bookings = [[1,2,10],[2,3,20],[2,5,25]]; n = 5
        assert [10,55,45,25,25] == solution.corpFlightBookings(bookings, n)

        bookings = [[1,2,10],[2,2,15]]; n = 2
        assert [10,25] == solution.corpFlightBookings(bookings, n)

        bookings = [[3,3,5],[1,3,20],[1,2,15]]; n = 3
        assert [35,35,25] == solution.corpFlightBookings(bookings, n)
