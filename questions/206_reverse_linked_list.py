# -*- coding:utf-8 -*-

class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:

	def reverseList(self, head: ListNode):
		if head is None or head.next is None:
			return head
		last_node = None
		while head != None:
			next_head = head.next
			head.next = last_node
			last_node = head
			head = next_head
		
		return last_node


	def reverseListRecursive(self, head: ListNode):
		if not head or head.next is None:
			return head
		new_head = self.reverseListRecursive(head.next)
		head.next.next = head
		head.next = None
		return new_head



class TestReverseList(object):

	"""
	pytest -s 206_reverse_linked_list.py::TestReverseList	
	"""

	def test(self):
		solution = Solution()
		head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
		new_head = solution.reverseList(head)
		assert 5 == new_head.val
		head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
		new_head = solution.reverseListRecursive(head)
		assert 5 == new_head.val
