# -*- coding:utf-8 -*-
from typing import List


class Solution:

	"""
	0/1背包问题
	给定 N 个物品，其中第 i 个物品的体积为 Vi, 价值为Wi
	有一容积为 M 的背包, 要求选择一些物品放入背包, 使得物品总体积不超过 M 的前提下, 物品的价值总和最大	

	F[i,j] 表示从前 i 个物品中选出了总体积为 j 的物品放入背包, 物品的最大价值和
	转移公式
		不选第 i 个物品, F[i-1, j]
		if j >= Vi, F[i-1, j-Vi] + Wi
		F[i,j] = max(F[i-1,j], F[i-1, j-Vi] + Wi if j >= Vi)
	初值: F[0,0] = 0, 其余负无穷
	目标: max (0<=j<=M) {F[N][j]}
	"""

	def dp_bag(self, n: int, m: int, v: List[int], w: List[int]):
		f = [[float("-inf")] * (m + 1) for _ in range(n + 1)]
		v.insert(0, 0)
		w.insert(0, 0)
		f[0][0] = 0
		for i in range(1, n + 1):
			# 不选第 i 个物品
			for j in range(0, m + 1):
				f[i][j] = f[i - 1][j]
			for j in range(v[i], m + 1):
				f[i][j] = max(f[i][j], f[i-1][j-v[i]] + w[i])

		print("f: %s" % f)
		ans = 0
		for j in range(0, m + 1):
			ans = max(ans, f[n][j])
		
		return ans


class Solution2:

	def dp_bag(self, n: int, m: int, v: List[int], w: List[int]):
		f = [float("-inf")] * (m + 1)
		v.insert(0, 0)
		w.insert(0, 0)
		f[0] = 0

		for i in range(1, n + 1):
			# j 必须倒序循环
			j = m
			while j >= v[i]:
				f[j] = max(f[j], f[j - v[i]] + w[i])
				j -= 1
		
		print("f: %s" % f)

		ans = 0
		for j in range(0, m+1):
			ans = max(ans, f[j])
		return ans


class TestDpBag:

	"""
	pytest -s dp_zero_one_bag.py::TestDpBag
	"""

	def test(self):
		solution = Solution2()

		# n 是三个物品, 背包最大重量为4, v 对应的是物品的重量, w 对应物品的价格
		n = 3; m = 4; v = [1, 3, 4]; w = [15, 20, 30]
		assert 35 == solution.dp_bag(n, m, v, w)
