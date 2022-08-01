# -*- coding:utf-8 -*-
from typing import List


class Solution:
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
