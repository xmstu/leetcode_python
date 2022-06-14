# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder
        return self.build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def build(self, l1, r1, l2, r2):
        if l1 > r1:
            return None
        root = TreeNode(self.preorder[l1])
        mid = l2
        while self.inorder[mid] != root.val:
            mid += 1
        root.left = self.build(l1 + 1, l1 + (mid - l2), l2, mid - 1)
        root.right = self.build(l1 + (mid - l2) + 1, r1, mid + 1, r2)
        return root
    

class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)



class TestBuildTree:

    """
    pytest -s 105_construct_binary_tree_from_preorder_and_inorder_traversal.py::TestBuildTree
    """

    def test(self):
        solution = Solution()
        solution2 = Solution2()

        preorder = [3,9,20,15,7] 
        inorder = [9,3,15,20,7]

        root = solution.buildTree(preorder, inorder)
        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.right.left.val == 15
        assert root.right.right.val == 7

        root = solution2.buildTree(preorder, inorder)
        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.right.left.val == 15
        assert root.right.right.val == 7

