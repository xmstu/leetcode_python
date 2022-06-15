# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    """
    对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(root: TreeNode):
            nonlocal ans
            # 递归边界
            if root is None:
                return [False, False]
            
            # 本层要做的事
            left_result = dfs(root.left)
            right_result = dfs(root.right)
            result = [False, False]
            result[0] = left_result[0] or right_result[0] or p.val == root.val
            result[1] = left_result[1] or right_result[1] or q.val == root.val

            # result 为 True 代表 该 子树 包含 p 和 q, 此时更新最近公共祖先
            if all(result) and ans is None:
                ans = root
            return result
        
        dfs(root)
        return ans


class TestLowestCommonAncestor:

    """
    pytest -s 236_lowest_common_ancestor_of_binary_tree.py::TestLowestCommonAncestor
    """

    def test(self):
        solution = Solution()

        root = TreeNode(3,
                        left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                        right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
        p = root.left
        q = root.right
        lca_node = solution.lowestCommonAncestor(root, p, q) 
        assert lca_node.val == 3

        p = root.left
        q = root.left.right.right
        lca_node = solution.lowestCommonAncestor(root, p, q) 
        assert lca_node.val == 5


