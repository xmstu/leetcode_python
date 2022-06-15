# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        return self.getNext(root, p.val)
    
    def getNext(self, root: TreeNode, val: int) -> TreeNode:
        ans = None
        curr = root
        while curr != None:
            # 找到当前的val, 并且当前节点的右子树不为空 
            if curr.val == val:
                if curr.right != None:
                    ans = curr.right
                    # 那么就找右子树中最小的点, 一直往右子树的左节点找
                    while ans.left != None:
                        ans = ans.left
            
            if val < curr.val:
                # 如果要找的值在左子树, 并且该值不存在右子树, 那么该值的后继节点在左子树经过节点的最小值
                if ans is None or ans.val > curr.val:
                    ans = curr
                curr = curr.left
            else:
                curr = curr.right

        return ans
    

    def inorderSuccessor2(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.ans = None
        self.getNextRecur(root, p.val)
        return self.ans
    
    def getNextRecur(self, root: TreeNode, val: int):
        # 递归终止条件
        if root is None:
            return

        # 本层要做的事
        if val < root.val:
            # 如果要找的值在左子树, 并且该值不存在右子树, 那么该值的后继节点在左子树经过节点的最小值
            if self.ans is None or self.ans.val > root.val:
                self.ans = root
            self.getNextRecur(root.left, val)
        elif val > root.val:
            self.getNextRecur(root.right, val)
        else:
            if root.right != None:
                self.ans = root.right
                while self.ans.left:
                    self.ans = self.ans.left 


class TestInorderSuccessor:
    """
    pytest -s 0406_inorder_successor.py::TestInorderSuccessor
    """

    def test(self):
        solution = Solution()

        root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
        assert 2 == solution.inorderSuccessor2(root, root.left).val

        root = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))
        assert None == solution.inorderSuccessor2(root, root.right)

        root = TreeNode(2, right=TreeNode(3))
        assert 3 == solution.inorderSuccessor2(root, root).val

