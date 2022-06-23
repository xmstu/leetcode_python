
from typing import List


def fib(n: int) -> List[int]:
	if n == 0:
		return [1]
	if n == 1:
		return [1, 1]
	ans = [1, 1]
	map = {0: 1, 1: 1}
	def recur(n):
		# 递归终止条件
		if n in map:
			return map[n]

		# 本层要做的事
		num = recur(n-1) + recur(n-2)
		map[n] = num
		ans.append(num)
		return num
	
	recur(n)
	
	return ans


def fib_func(n: int):
	map = {0: 1, 1: 1}

	def recur(n):
		# 递归终止条件
		if n in map:
			return map[n]

		# 本层要做的事
		num = recur(n-1) + recur(n-2)
		map[n] = num
		return num
	for i in range(n+1):
		yield recur(i)


class TestFib:

	"""
	pytest -s fib.py::TestFib
	"""

	def test(self):

		"""
		请用递归函数的形式将斐波那契(fib)表现出来,前两个数分别是1, 1

		提示

		def fib(n=100) 
		for i in fib(n=100):
			print(i) 

		要求：
		1、 fib直接生成一个序列
		2、 放在一个函数里，即，只能用一个函数去实现
		3、 函数内没有嵌套（加分项）
		"""
		
		for i in fib_func(n=100):
			print(i)

