# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def __init__(self) -> None:
        # 记忆算过的答案, 不再重复算
        self.store = dict()

    def generateParenthesis(self, n: int) -> List[str]:
        """
        括号构成: 默认 () 包着 A 个 括号, 右边是 B 个括号
        S = (A)B
        A = k - 1, B = n - K, 再加上包着 A 个括号的外层括号一个, 加起来就是 n 个括号

        k = 1 (A) A = 0 对括号: ()  B=n-k=2 对括号, B 有两种情况: ()(), (())
        组合起来: ()()(), ()(())

        k = 2 (A) A=1 对括号: (()), B=n-k=1 对括号, B 只有一种情况: ()
        组合起来: (())()

        k = 3 (A) A=2 对括号: (()()), ((())), B=n-k=0 对括号
        组合起来: (()()), ((()))

        加起来就有 5 种情况
        """
        # 递归终止条件
        if n == 0:
            return [""]
        
        if self.store.get(n):
            return self.store[n]
        
        # 结果数组
        ans = []

        # 每层要做的事
        for k in range(1, n+1):
            # 加法原理
            A = self.generateParenthesis(k-1)
            B = self.generateParenthesis(n-k)
            # S = (A)B
            print("A: %s, B: %s, k: %s" % (A, B, k))
            # 乘法原理
            for a in A:
                for b in B:
                    ans.append("(" + a + ")" + b)
        
        self.store[n] = ans
        return ans


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        利用dfs的思想, 递归地生成括号
        """

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            # 右括号个数小于左括号, 需要剪枝, 不能再增加左括号了
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


class TestGenerateParenthesis:

    """
    pytest -s 22_generate_parentheses.py::TestGenerateParenthesis
    """

    def test(self):
        solution = Solution()

        n = 3
        assert ["()()()", "()(())", "(())()", "(()())", "((()))"] == solution.generateParenthesis(n)

        n = 1
        assert ["()"] == solution.generateParenthesis(n)
