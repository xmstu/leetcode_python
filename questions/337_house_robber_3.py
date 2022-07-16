# -*- coding:utf-8 -*-
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root。
    除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
    给定二叉树的 root。返回在不触动警报的情况下, 小偷能够盗取的最高金额

    思路:
        f[x, 0] 表示以 x 为根的子树, 在不打劫 x 的情况下, 能盗取的最高金额
        f[x, 1] 表示以 x 为根的子树, 在打劫 x 的情况下, 能盗取的最高金额

        偷了父节点, 就不能偷子节点, 类似的, 父节点不偷, 子节点可偷可不偷, 有两种分支
        方程:f[x, 1] = val(x) + f[y, 0] # y is son of x
        方程:f[x, 0] = max(f[y, 0], f[y, 1]) # y is son of x

    """
    def rob(self, root: TreeNode) -> int:
        f = defaultdict(lambda : [0, 0])

        def dfs(root: TreeNode):
            # 递归终止条件
            if root is None:
                return
            
            dfs(root.left)
            dfs(root.right)

            f[root][0] = max(f[root.left][0], f[root.left][1]) + max(f[root.right][0], f[root.right][1])
            f[root][1] = root.val + f[root.left][0] + f[root.right][0]

        dfs(root)

        print("f: %s" % f)

        return max(f[root][0], f[root][1])



class TestRob:

    """
    pytest -s 337_house_robber_3.py::TestRob
    """

    def test(self):

        solution = Solution()

        root = TreeNode(3,
                        left=TreeNode(2, right=TreeNode(3)),
                        right=TreeNode(3, right=TreeNode(1)),
                        )
        assert 7 == solution.rob(root)

        root = TreeNode(3,
                        left=TreeNode(4, left=TreeNode(1), right=TreeNode(3)),
                        right=TreeNode(5, right=TreeNode(1)),
                        )
        assert 9 == solution.rob(root)
