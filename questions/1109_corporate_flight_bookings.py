# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    这里有 n 个航班, 它们分别从 1 到 n 进行编号。
    有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
    请你返回一个长度为 n 的数组 answer, 里面的元素是每个航班预定的座位总数。
    """
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pass


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
