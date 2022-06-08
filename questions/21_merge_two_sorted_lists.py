# -*- coding:utf-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 用一个哑节点用于最后返回新的头节点
        dummy_head = ListNode(-1)
        # prev 节点需要不断向后移动
        prev = dummy_head
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
                
        # 在最后处理还有一个链表还有节点的情况
        prev.next = list1 if list1 else list2

        return dummy_head.next


class TestMergeTwoLists:

    """
    pytest -s 21_merge_two_sorted_lists.py::TestMergeTwoLists
    """

    def test(self):
        solution = Solution()

        head_l1 = ListNode(1, ListNode(2, ListNode(4)))
        head_l2 = ListNode(1, ListNode(3, ListNode(4)))
        new_head = solution.mergeTwoLists(head_l1, head_l2)
        res = []
        while new_head:
            res.append(new_head.val)
            new_head = new_head.next
        assert res == [1,1,2,3,4,4]

        head_l1 = head_l2 = None
        assert None == solution.mergeTwoLists(head_l1, head_l2)

        head_l1 = None
        head_l2 = ListNode(0)
        new_head = solution.mergeTwoLists(head_l1, head_l2)
        assert head_l2 == new_head



