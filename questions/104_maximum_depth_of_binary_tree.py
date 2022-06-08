# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        自底向上
        """
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0

    def maxDepthFromTopToBottom(self, root: Optional[TreeNode]) -> int:
        """
        自顶向下
        """
        self.depth = 1
        self.ans = 0
        self.calc(root)
        return self.ans
        
    def calc(self, root: TreeNode):
        # 递归终止条件
        if root is None:
            return
        
        # 本层要做的事, 每遍历一层加 1
        # 每次更新 答案
        self.ans = max(self.ans, self.depth)
        # 来到新的一层, depth + 1
        self.depth += 1
        # 递归 左右 子树
        self.calc(root.left)
        self.calc(root.right)

        # 还原现场: 回到上一层, depth - 1
        self.depth -= 1


class TestMaxDepth:

    """
    pytest -s 104_maximum_depth_of_binary_tree.py::TestMaxDepth
    """

    def test(self):
        solution = Solution()

        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert 3 == solution.maxDepth(root)

        root = TreeNode(1, None, TreeNode(2))
        assert 2 == solution.maxDepth(root)

        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert 3 == solution.maxDepthFromTopToBottom(root)

        root = TreeNode(1, None, TreeNode(2))
        assert 2 == solution.maxDepthFromTopToBottom(root)




