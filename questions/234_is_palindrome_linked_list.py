# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-26
    :Copyright: (c) 2021, hexm
"""

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution(object):

    def isPalindromeByArray(self, head: ListNode) -> bool:
        """[summary]

        Args:
            head (ListNode): [传入的链表头]

        Returns:
            bool: [description]
        """
        arr = []
        current_node = head
        while current_node is not None:
            arr.append(current_node.val)
            current_node = current_node.next
        
        return arr == arr[::-1]
    
    def isPalindromeByFastSlowIndex(self, head: ListNode) -> bool:
        """[通过快慢指针来判断是否回文链表]
        通过快慢指针判断是否为回文链表，因为快指针比慢指针走快一步，当快指针走到链表尽头，慢指针应该刚好走到快指针的一半，即链表中间

        Args:
            head (ListNode): [链表头]

        Returns:
            bool: [description]
        """

        if head is None:
            return True
        
        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        print("first_half_end.val: %s" % first_half_end.val)
        print("second_half_start.val: %s" % second_half_start.val)

        # 判断是否回文
        result = True
        first_pos = head
        second_pos = second_half_start
        while result and second_pos is not None:
            print('now first_pos.val: %s, second_pos.val: %s' % (first_pos.val, second_pos.val))
            if first_pos.val != second_pos.val:
                result = False
            
            first_pos = first_pos.next
            second_pos = second_pos.next
            print('next first_pos.val: %s, second_pos.val: %s' % (first_pos.val, second_pos.val if isinstance(second_pos, ListNode) else second_pos))

        # 还原后半部分链表，不破坏原来链表的结构 
        first_half_end.next =  self.reverse_list(second_half_start)

        return result
    
    def end_of_first_half(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        反转链表
        """
        previous = None
        cur = head
        while cur is not None:
            next_node = cur.next
            cur.next = previous
            previous = cur
            cur = next_node

        return previous
    

class TestIsPalindrome(object):
    """
    pytest -s is_palindrome.py::TestIsPalindrome
    """

    def test_solution(self):
        root = ListNode(
            val=1, 
            next=ListNode(
                val=3,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=1,
                        next=None
                    )
                )
            ) 
        )

        solution = Solution()
        ok = solution.isPalindromeByArray(root)
        print("ok: %s" % ok)
        assert ok == True

        ok = solution.isPalindromeByFastSlowIndex(root)
        print("ok: %s" % ok)
        assert ok == True



