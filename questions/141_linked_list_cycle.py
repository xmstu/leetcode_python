# -*- coding:utf-8 -*-
from typing import Optional



class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_head = head
        slow_head = head
        while fast_head and fast_head.next:
            fast_head = fast_head.next.next
            slow_head = slow_head.next
            if fast_head == slow_head:
                return True
        return False


class TestHasCycle:
    """
    pytest -s 141_linked_list_cycle.py::TestHasCycle
    """

    def test(self):
        solution = Solution()

        head = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        assert True == solution.hasCycle(head)
