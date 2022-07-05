# -*- coding:utf-8 -*-


class Solution:
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    """
    def climbStairs(self, n: int) -> int:
        """
        动态规划
            状态转移方程: f{n}=f{n-1)+f(n-2)
        """
        p, q, r = 0, 0, 1
        for i in range(1, n+1):
            p = q
            q = r
            r = p + q
        return r
   

class Solution2:
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    """
    def climbStairs(self, n: int) -> int:
        """
        dfs 记忆化搜索
        """
        memory_dict = {}
        memory_dict[1] = 1
        memory_dict[2] = 2
        def dfs(n: int):
            if n in memory_dict:
                return memory_dict[n]
            memory_dict[n] = dfs(n - 1) + dfs(n - 2)
            return memory_dict[n]
        
        res = dfs(n) 
        return res


class TestClimbStairs:

    """
    pytest -s 70_climbing_stairs.py::TestClimbStairs
    """

    def test(self):
        solution = Solution2()

        assert 2 == solution.climbStairs(2)
        assert 3 == solution.climbStairs(3)
        assert 63245986 == solution.climbStairs(38)
