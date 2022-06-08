# -*- coding:utf-8 -*-
"""
    :Author: hexm
    :Created Date: 2021-07-19
    :Copyright: (c) 2021, hexm
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
        例如：
        给定二叉树 [3,9,20,null,null,15,7]
            3
           / \
          9  20
            /  \
           15   7
        返回锯齿形层序遍历如下:
         [
          [3],
          [20,9],
          [15,7]
         ]
        思路:
            1. 在遍历二叉树的时候，判断是奇数层还是偶数层
            2. 如果是奇数层，则从左往右遍历，如果是偶数层，则从右往左
        :param root:
        :return:
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        is_order_left = True
        result = []
        while q:
            q_size = len(q)
            temp = []
            # 将当前层的节点加入temp，并将下一层的节点加入 q, 下一层节点继续循环
            for i in range(q_size):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 从左往右直接加入结果
            if is_order_left:
                result.append(temp)
            # 从右往左将temp反转后加入结果
            else:
                result.append(temp[::-1])

            # 每次循环结束后更新标志位
            is_order_left = not is_order_left
        return result


class TestZigzagLevelOrder(object):
    """
    执行命令跑单测:  pytest -s zigzag_level_order.py::TestZigzagLevelOrder
    """

    def test_solution(self):
        root_node = TreeNode(
            val=3,
            left=TreeNode(val=9, left=TreeNode(val=10), right=TreeNode(val=1)),
            right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)),
        )
        solution = Solution()
        rs = solution.zigzagLevelOrder(root_node)
        expect_rs = [[3], [20, 9], [10, 1, 15, 7]]
        print("rs: %s, expect_rs: %s" % (rs, expect_rs))
        assert rs == expect_rs
