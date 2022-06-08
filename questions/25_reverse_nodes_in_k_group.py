# -*- coding:utf-8 -*-
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        protect = ListNode(0, head)
        last = protect
        while head != None:
            # 1. 分组遍历（往后走 k - 1 步, 返回一组的结尾end）
            end = self.getEnd(head, k)
            if end is None:
                break
            nextGroupHead = end.next
            # 2. 反转每组的内部的边（调用反转链表）
            self.reverseList(head, nextGroupHead)
            # 3. 更新每组跟前一组，后一组的边
            last.next = end
            head.next = nextGroupHead
            last = head
            head = nextGroupHead
        return protect.next
    
    def getEnd(self, head: ListNode, k: int):
        # head == None 就终止遍历, 够 k 个的返回 head, 不够的返回 None
        while head != None:
            k -= 1
            if k == 0:
                return head
            head = head.next
        return None

    def reverseList(self, head: ListNode, stop: ListNode):
        # 先提前遍历一步, 因为last不需要指向空
        last = head
        head = head.next
        while head != stop:
            next_head = head.next
            head.next = last
            last = head
            head = next_head


class TestReverseKGroup:

    """
    pytest -s 25_reverse_nodes_in_k_group.py::TestReverseKGroup
    """
    def test(self):
        solution = Solution()
        node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        new_head = solution.reverseKGroup(node, 2)
        s = ""
        while new_head:
            s += str(new_head.val)
            new_head = new_head.next
        print("fuck s: %s" % s)
        assert s == "21435"
