# -*- coding:utf-8 -*-
from typing import List


class Solution:

	"""
	在一条数轴上有 N 家商店，它们的坐标分别为 A1~AN。
	现在需要在数轴上建立一家货仓，每天清晨，从货仓到每家商店都要运送一车商品。
	为了提高效率，求把货仓建在何处，可以使得货仓到每家商店的距离之和最小。

	输出:
		输出一个整数，表示距离之和的最小值。
	
	思路, 中位数下标的数轴就是距离之和最小值的货仓位置
	"""

	def warehouse_address(self, n: int, array: List[int]) -> int:
		array.sort()
		pos = array[n >> 1]
		ans = 0
		for i in range(n):
			ans += abs(pos - array[i])
		
		return ans


class TestWarehouseAddress:

	"""
	pytest -s acwing_104_warehouse_address_selection.py::TestWarehouseAddress
	"""

	def test(self):
		solution = Solution()

		n = 4; array = [6,2,9,1]
		assert 12 == solution.warehouse_address(n, array)

