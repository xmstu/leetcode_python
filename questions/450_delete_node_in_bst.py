# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 递归终止条件
        if root is None:
            return None
        
        # 本层要做的事
        # 如果相等
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 如果当前节点左右都有节点, 那么就要找当前节点的后继节点
            next = root.right
            while next.left:
                next = next.left
            # 找到后继节点后, 在当前节点的右子树中删去后继节点
            root.right = self.deleteNode(root.right, next.val)
            # 并将当前节点的值赋值为后继节点的值
            root.val = next.val
            return root
        
        # 递归删除
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


class TestDeleteNode:

    """
    pytest -s 450_delete_node_in_bst.py::TestDeleteNode
    """

    def test(self):
        solution = Solution()

        root = TreeNode(5, left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)), right=TreeNode(6, right=TreeNode(7)))
        new_root = solution.deleteNode(root, 5)
        assert new_root.val == 6
