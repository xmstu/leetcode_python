# -*- coding:utf-8 -*-


class BinaryHeap:

	"""
	两种做法:
		假设第一个元素存在下标 1
			- 索引p节点的左孩子索引为 p * 2
			- 索引p节点的右孩子索引为 p * 2 + 1
			- 索引p的父亲索引为 p / 2 (下取整)
		假设第一个元素存在下标 0
			- 索引p节点的左孩子索引为 p * 2 + 1
			- 索引p节点的右孩子索引为 p * 2 + 2
			- 索引p的父亲索引为 (p-1) / 2 (下取整)
	"""

	def __init__(self) -> None:
		self.heap = []
	
	def empty(self):
		return True if not self.heap else False
	
	def top(self):
		return self.heap[0] if not self.empty() else None
	
	def push(self, item):
		self.heap.append(item)
		self.heapifyUp(len(self.heap)-1)
	
	def pop(self):
		if self.empty():
			return
		# 删除堆顶, 就将堆顶的值等于列表的末尾值, 删去列表的末尾, 并进行 heapifydown 
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		self.heapifyDown(0)

	def heapifyUp(self, p):
		while p > 0:
			if self.heap[p] < self.heap[(p-1) // 2]:
				self.heap[p], self.heap[(p-1) // 2] = self.heap[(p-1) // 2], self.heap[p]
				p = (p - 1) // 2
			else:
				break

	def heapifyDown(self, p):
		heap_size = len(self.heap)
		child = p * 2 + 1
		while child < heap_size:
			other = p * 2 + 2
			if other < heap_size and self.heap[other] < self.heap[child]:
				child = other
			if self.heap[child] < self.heap[p]:
				self.heap[p], self.heap[child] = self.heap[child], self.heap[p]
				p = child
				child = p * 2 + 1
			else:
				break


class TestMyheapq:

	"""
	pytest -s my_heaq.py::TestMyheapq
	"""

	def test(self):
		pq = BinaryHeap()

		pq.push(1)
		pq.push(9)
		pq.push(4)
		pq.push(2)
		pq.push(6)
		pq.push(7)

		assert 1 == pq.top()
		pq.pop()
		assert 2 == pq.top()
		pq.pop()
		assert 4 == pq.top()
		pq.push(1)
		assert 1 == pq.top()
		print(pq.heap)
		pq.pop()
		pq.pop()
		pq.pop()
		pq.pop()
		pq.pop()
		assert pq.empty() == True
