# -*- coding:utf-8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归停止条件
        if root is None:
            return

        # 每层需要做的事情
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        # 所有递归调用结束, 回到第一层调用, 返回root即可
        return root


def front(root: TreeNode, result: List):
    if root is None:
        return
    
    result.append(root.val)
    front(root.left, result)
    front(root.right, result)

    return root


class TestInvertTree:

    """
    pytest -s 226_invert_binary_tree.py::TestInvertTree
    """

    def test(self):
        solution = Solution()

        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))    
        solution.invertTree(root)
        result = []
        front(root, result)
        assert [4,7,9,6,2,3,1] == result

        root = TreeNode(2, TreeNode(1), TreeNode(3))    
        solution.invertTree(root)
        result = []
        front(root, result)
        assert [2,3,1] == result

