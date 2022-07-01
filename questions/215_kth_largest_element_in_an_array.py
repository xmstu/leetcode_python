# -*- coding:utf-8 -*-
from typing import List
import random


class BinaryHeap:

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
        raise NotImplementedError()
    
    def heapifyDown(self, p):
        raise NotImplementedError()


class BigRootHeap(BinaryHeap):

    def heapifyUp(self, p):
        while p > 0:
            if self.heap[p] > self.heap[(p-1) // 2]:
                self.heap[p], self.heap[(p-1) // 2] = self.heap[(p-1) // 2], self.heap[p]
                p = (p - 1) // 2
            else:
                break

    def heapifyDown(self, p):
        heap_size = len(self.heap)
        child = p * 2 + 1
        while child < heap_size:
            other = p * 2 + 2
            if other < heap_size and self.heap[other] > self.heap[child]:
                child = other
            if self.heap[child] > self.heap[p]:
                self.heap[p], self.heap[child] = self.heap[child], self.heap[p]
                p = child
                child = p * 2 + 1
            else:
                break


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        直接快排, 时间复杂度 O(NlogN)
        """
        nums.sort()
        return nums[len(nums) - k]
    
    def findKthLargestHeapq(self, nums: List[int], k: int) -> int:
        """
        构建一个大根堆, pop出第 k 个堆顶, 就是第 k 大元素
        """
        big_root_heap = BigRootHeap()
        for num in nums:
            big_root_heap.push(num)
        
        kth_largest_num = None
        for _ in range(k):
            kth_largest_num = big_root_heap.top()
            big_root_heap.pop()
        return kth_largest_num
    
    def findKthLargestQuickSort(self, nums: List[int], k: int) -> int:
        """
        快排
        """
        # 时间复杂度 O(N)
        return self.quickSort(nums, 0, len(nums) - 1, len(nums) - k)
    
    def quickSort(self, arr: List[int], left: int, right: int, index: int):
        if left >= right:
            return arr[left]
        pivot = self.partition(arr, left, right)
        # 如果 第 k 大的 index 小于等于基准的index, 那么去左半区间找, 否则去右半区间
        if index <= pivot:
            return self.quickSort(arr, left, pivot, index)
        else:
            return self.quickSort(arr, pivot + 1, right, index)

    def partition(self, arr: List[int], left: int, right: int):
        pivot = random.randint(left, right)
        pivotVal = arr[pivot]

        while left <= right:
            while arr[left] < pivotVal:
                left += 1
            while arr[right] > pivotVal:
                right -= 1
            # if left == right:
            #     break
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        return right
    


class TestFindKthLargest:

    """
    pytest -s 215_kth_largest_element_in_an_array.py::TestFindKthLargest
    """

    def test(self):
        solution = Solution()
        nums = [3,2,1,5,6,4]; k = 2
        assert 5 == solution.findKthLargestHeapq(nums, k)

        nums = [3,2,3,1,2,4,5,5,6]; k = 4
        assert 4 == solution.findKthLargest(nums, k)

        nums = [3,2,1,5,6,4]; k = 2
        assert 5 == solution.findKthLargestQuickSort(nums, k)
