# -*- coding:utf-8 -*-
from typing import List


class Solution:

	"""
	完全背包问题
	给定 N 个物品，其中第 i 个物品的体积为 Vi, 价值为Wi, 并且每件物品无数个, 和 0/1 背包不同在于每个物品数量无限个, 可以重复选
	有一容积为 M 的背包, 要求选择一些物品放入背包, 使得物品总体积不超过 M 的前提下, 物品的价值总和最大	

	F[i,j] 表示从前 i 个物品中选出了总体积为 j 的物品放入背包, 物品的最大价值和
	转移公式
		不选第 i 个物品, F[i-1, j]
		if j >= Vi, F[i, j-Vi] + Wi
		F[i,j] = max(F[i-1,j], F[i-1, j-Vi] + Wi if j >= Vi)
	初值: F[0,0] = 0, 其余负无穷
	目标: max (0<=j<=M) {F[N][j]}
	"""

	def dp_bag(self, n: int, m: int, v: List[int], w: List[int]):
		f = [float("-inf")] * (m + 1)
		v.insert(0, 0)
		w.insert(0, 0)
		f[0] = 0

		for i in range(1, n + 1):
			# j 正着循环, 就是完全背包, 因为每个位置都会被重复算
			for j in range(v[i], m + 1):
				f[j] = max(f[j], f[j - v[i]] + w[i])
		
		print("f: %s" % f)

		ans = 0
		for j in range(0, m+1):
			ans = max(ans, f[j])
		return ans


class TestDpBag:

	"""
	pytest -s dp_full_bag.py::TestDpBag
	"""

	def test(self):
		solution = Solution()

		# n 是三个物品, 背包最大重量为4, v 对应的是物品的重量, w 对应物品的价格
		n = 3; m = 4; v = [1, 3, 4]; w = [15, 20, 30]
		assert 60 == solution.dp_bag(n, m, v, w)
