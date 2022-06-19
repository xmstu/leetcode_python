# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: TreeNode):
            nonlocal total
            if root is None:
                return
            dfs(root.right)
            total += root.val
            root.val = total
            dfs(root.left)
        
        total = 0
        dfs(root)
        return root


class TestConvertBST:

    """
    pytest -s 538_convert_bst_to_greater_tree.py::TestConvertBST
    """

    def test(self):
        solution = Solution()

        root = TreeNode(4,
                        left=TreeNode(1, left=TreeNode(0), right=TreeNode(2, right=TreeNode(3))),
                        right=TreeNode(6, left=TreeNode(5), right=TreeNode(7, right=TreeNode(8))),
        )
        new_root = solution.convertBST(root)

        assert new_root.val == 30

        assert new_root.left.val == 36
        assert new_root.left.left.val == 36
        assert new_root.left.right.val == 35
        assert new_root.left.right.right.val == 33

        assert new_root.right.val == 21
        assert new_root.right.left.val == 26
        assert new_root.right.right.val == 15
        assert new_root.right.right.right.val == 8
