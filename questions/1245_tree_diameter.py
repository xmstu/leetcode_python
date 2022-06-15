# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:

	"""
	给出一棵无向树, 求树的最长直径
	无向树就是没有指定根的树, 可以以任意一个节点作为根

	解法:
		两次 DFS
			第一次从任意一点出发, 找到距离它最远的点 p
			第二次从 p 出发, 找到距离它最远的点 q
			pq的路径就是最长直径
		反证法:
			1. 假设 q 是最长直径的一端;
			2. 任意一点为 s, s->p 是离s最远的路径;
			3. 假设 p 不是直径另一端, r才是直径另一端;
			4. 那么 s->p 和 r->q 会相交于 x;
			5. 因为 s->p 是 s 最长路径, x->p 应该长于 x->r;
			6. 但因为 r->q 才是最长直径, x->r 应该长于 x->p;
			7. 两个结论自相矛盾, 因此反证得 p 是最长直径一端;
	"""

	def treeDiameter(self, edges: List[List[int]]) -> int:
		n = 0
		# 求出点的最大编号
		for edge in edges:
			x, y = edge[0], edge[1]
			n = max(n, max(x, y))
		# 最大编号 + 1 就是求得共有多少个点
		n += 1
		self.n = n
		# 开辟一个出边数组
		to = []
		for _ in range(n):
			to.append([])
		for edge in edges:
			x, y = edge[0], edge[1]
			to[x].append(y)
			to[y].append(x)
		self.to = to	
		p = self.findFarthest(0)[0]
		print("p: %s" % p)
		return self.findFarthest(p)[1]
	
	def findFarthest(self, start) -> List[int]:
		"""
		返回一个列表, 列表得第一个值是点, 第二个值是 start 到 最远点的距离
		"""
		depth = [-1 for _ in range(self.n)]
		q = deque()
		q.appendleft(start)
		depth[start] = 0
		while q:
			x = q.pop()
			for y in self.to[x]:
				if depth[y] != -1:
					continue
				depth[y] = depth[x] + 1
				q.appendleft(y)
		ans = start
		for i in range(self.n):
			if depth[i] > depth[ans]:
				ans = i
		print("depth: %s, ans: %s" % (depth, ans))
		return [ans, depth[ans]]


class TestTreeDiameter:

	"""
	pytest -s 1245_tree_diameter.py::TestTreeDiameter
	"""

	def test(self):
		solution = Solution()

		edges = [[0,1],[0,2]]
		assert 2 == solution.treeDiameter(edges)

		edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
		assert 4 == solution.treeDiameter(edges)
