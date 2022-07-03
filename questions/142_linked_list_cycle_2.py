# -*- coding:utf-8 -*-
from typing import Optional



class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    返回入环点
    - 思路
        1. 如果是通过break退出，则第一次相遇
        2. 已知slow速度为1 ， fast速度为2
        3. 设 环长是m, 起点到入环口距离为x, fast指针从入环口出来追上slow指针的距离是y
        4. fast指针走的路程：x + y + m ；  m 表示刚好多走了一圈环长
        5. slow指针走的路程：x + y
        6. 由于存在2倍速度差, slow节点走的距离乘以2就是fast节点走的距离: 得到 2(x+y) = x + y + m
        7. 其中又因为 m 可再分解为 (m - y) + y
        8. 得到 2x + 2y = x + 2y + (m - y)
        9. 得到 x = m - y
        10. 说明此时fast、slow指针所处位置继续前进到入环口的距离 与 起点走到入环口的距离恰好相等
        11. 所以任意将一个指针返回头节点，然后两个指针以相同的速度移动，下次就会在入环口相遇
    :return:
    """
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        # 如果fast为None或fast无下一个节点，则无环
        if fast is None or fast.next is None:
            return None
        # 快节点和慢节点相遇后, 选取任一节点从头开始跑, 步长都为1, 再走 m - y 步, 两节点就会相遇
        fast = head
        while True:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next
        return fast


class TestDetectCycle:
    """
    pytest -s 142_linked_list_cycle_2.py::TestDetectCycle
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
        assert node2 == solution.detectCycle(head)
