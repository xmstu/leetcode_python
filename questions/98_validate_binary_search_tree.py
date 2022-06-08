# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recur(root, float("-inf"), float("inf"))

    def recur(self, root: TreeNode, leftVal: int, rightVal: int):
        # 递归终止条件
        if root is None:
            return True
        
        # 当前这层要做的事情
        if not (leftVal < root.val < rightVal):
            return False
        
        return self.recur(root.left, leftVal, root.val) and self.recur(root.right, root.val, rightVal)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        中序遍历, 迭代版本
        """
        stack, inorder = [], float('-inf')
        
        # 中序遍历, 因为二叉搜索树中序遍历得到的是升序的数组
        # 因此可以在中序遍历的时候判断当前节点的值是否小于上一个节点的值, 是的话就不是二叉搜索树 
        # 全部遍历完都没有小于的情况就是二叉搜索树
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
    
class Solution3:

    def __init__(self) -> None:
        self.pre = float("-inf")

    def isValidBST(self, root: TreeNode) -> bool:
        """中序遍历, 递归版本"""
        # 递归终止条件
        if root is None:
            return True
        
        # 本层要比较当前节点的值和上一个节点的值
        # 访问左子树
        if not self.isValidBST(root.left):
            return False
        
        # 当前节点的值与前一个值比较
        if root.val <= self.pre:
            return False
        
        self.pre = root.val

        # 访问右子树
        return self.isValidBST(root.right)


class TestIsVaildBST:

    """
    pytest -s 98_validate_binary_search_tree.py::TestIsVaildBST
    """

    def test(self):
        solution = Solution()

        root = TreeNode(2, TreeNode(1), TreeNode(3))
        assert True == solution.isValidBST(root)

        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        assert False == solution.isValidBST(root)



