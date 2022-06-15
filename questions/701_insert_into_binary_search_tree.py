# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 递归边界, 到了空节点, 说明找到可以插入节点的位置, 返回即可
        if root is None:
            return TreeNode(val)
        
        # val 小于 根节点, 就在左子树种找插入位置, 大于根节点, 就在右子树找插入位置
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root


class TestInsertIntoBST:

    """
    pytest -s 701_insert_into_binary_search_tree.py::TestInsertIntoBST
    """

    def test(self):
        solution = Solution()

        root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
        new_root = solution.insertIntoBST(root=root, val=5)
        assert new_root.right.left.val == 5
