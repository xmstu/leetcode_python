# -*- coding:utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def myBuildTree(in_left, in_right):
            # 如果这里没有节点构造二叉树, 就结束
            if in_left > in_right:
                return None
            
            # 后序遍历的数组尾部元素就是根节点
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # 根据 root 所在位置分为左右两棵子树
            index = inorder_index[root_val]  # 在中序遍历数组中根的index
            print("index: %s, root_val: %s, in_left: %s, in_right: %s" % (index, root_val, in_left, in_right))

            # 构建右子树, 需要先构建右子树, 因为后序遍历是 左右根, 那么 pop 的时候, 是先将右子树的根 pop 出来
            root.right = myBuildTree(index + 1, in_right)
            # 构建左子树
            root.left = myBuildTree(in_left, index - 1)

            return root

        inorder_index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, len(inorder) - 1)


class TestBuildTree:

    """
    pytest -s 106_construct_binary_tree_from_inorder_and_postorder_traversal.py::TestBuildTree
    """

    def test(self):
        solution = Solution()

        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]

        root = solution.buildTree(inorder, postorder)
        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.right.left.val == 15
        assert root.right.right.val == 7
