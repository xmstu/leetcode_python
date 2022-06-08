# -*- coding:utf-8 -*-
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        递推法: 一个一个合并
        时间复杂度: O(k^2 * n)
        空间复杂度: O(1)
        """
        res = None
        for l in lists:
            res = self.mergeTwoLists(res, l)
        
        return res
    
    def mergeKListsDivdeAndConquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        分治法, 将列表不断分割, 直到只剩一个, 再两两合并
        渐进时间复杂度为 O(kn * log k)
        递归用了栈, 因此空间复杂度为: O(log k)
        """
        n = len(lists)
        # 递归终止条件
        if n == 1:
            return lists[0]
        if n == 0:
            return None
        # 每层要做的事
        left_list = self.mergeKListsDivdeAndConquer(lists[:n // 2])
        right_list = self.mergeKListsDivdeAndConquer(lists[n // 2:])
        # 合并左和右链表
        new_head = self.mergeTwoLists(left_list, right_list)

        return new_head 
    
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


class TestMergeKSortedLists:
    """
    pytest -s 23_merge_k_sorted_lists.py::TestMergeKSortedLists
    """

    def test(self):
        solution = Solution()

        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        node = solution.mergeKListsDivdeAndConquer(lists)
        res = []
        while node:
            res.append(node.val)
            node = node.next
        assert [1,1,2,3,4,4,5,6] == res

        assert None == solution.mergeKListsDivdeAndConquer([])

        assert None == solution.mergeKListsDivdeAndConquer([None])

