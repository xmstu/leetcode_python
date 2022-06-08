# -*- coding:utf-8 -*-
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Todo 分治法
        res = None
        for l in lists:
            res = self.mergeTwoLists(res, l)
        
        return res
    
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
