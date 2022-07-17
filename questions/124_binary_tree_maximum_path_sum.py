# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum = -1e9

        def dfs(root: TreeNode) -> int:
            nonlocal pathSum
            # 递归终止条件
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            # 本层要做的事, dp 转移
            # 本节点的值 和 本节点与左右节点中最大的路径和构成的一条路径和比较
            ret = max(root.val, root.val + max(left, right))
            # 最大路径和, 再比较 ret 和 本节点的值加上左右两个路径的和得到最大值
            pathSum = max(pathSum, ret, root.val + left + right)
            return ret
        dfs(root)
        return pathSum


class TestMaxPathSum:

    """
    pytest -s 124_binary_tree_maximum_path_sum.py::TestMaxPathSum
    """

    def test(self):
        solution = Solution()

        root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
        assert 6 == solution.maxPathSum(root)

        root = TreeNode(-10, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
        assert 42 == solution.maxPathSum(root)

