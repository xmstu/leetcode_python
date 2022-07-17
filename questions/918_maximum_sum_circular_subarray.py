# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class Solution:
    """
    给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
    环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
    子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。

    思路:
        方法一
            最大子序和, 是对每一个s[i], 找它前面最小的s[j], 其中s是前缀和, 也就是 f[i] = s[i] - min(s[j]) (0<=j<i)
            目标 max(f[i]) (1<=i<=n)
            把数组看成线性(1~n), 然后复制一倍接在后面, 变成长度为2n的数组, 求前缀和
            f[i] = s[i] - min(s[j]) (i-n<=j<i)
            目标 max(f[i]) (1<=i<=2n)
            用滑动窗口最小值解决

    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 0)
        ss = [0] * (2 * n + 1)
        for i in range(1, n + 1):
            ss[i] = ss[i - 1] + nums[i]
        for i in range(n + 1, 2 * n + 1):
            ss[i] = ss[i - 1] + nums[i - n]
        
        # 单调队列, 单调递增队列, 队头最小, 队尾最大
        q = deque()
        ans = -1e9
        for i in range(1, 2 * n + 1):
            # 维护队头
            while q and q[0] < i - n:
                q.popleft()
            # 更新答案
            if q:
                ans = max(ans, ss[i] - ss[q[0]])
            # 维护单调递增的队列
            while q and ss[q[-1]] >= ss[i]:
                q.pop()
            q.append(i)
        
        return ans


class Solution2:

    """
    思路:
        方法二
            最大子序和跨域了 1 - n

            - 等价于开头取一段, 结尾取一段, 和最大
            - 等价于 总和 减去 中间取一段, 和最小
            - total_sum - 按线性数组求最小子序和

            最终答案: max(数组的最大子序和, total_sum - 数组的最小子序和)
    """

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 0)
        s = [0] * (n + 1)
        for i in range(1, n+1):
            s[i] = s[i - 1] + nums[i]
        temp = 1e9
        ans = -1e9
        for i in range(1, n+1):
            temp = min(temp, s[i - 1])
            ans = max(ans, s[i] - temp)

        temp = -1e9 
        ansMin = 1e9
        for i in range(2, n+1):
            temp = max(temp, s[i - 1])
            ansMin = min(ansMin, s[i] - temp)
        
        for i in range(1, n):
            ansMin = min(ansMin, s[i])

        return max(ans, s[n] - ansMin)


class TestMaxSubarraySumCircular:

    """
    pytest -s 918_maximum_sum_circular_subarray.py::TestMaxSubarraySumCircular
    """

    def test(self):
        solution = Solution()

        nums = [1,-2,3,-2]
        assert 3 == solution.maxSubarraySumCircular(nums)

        nums = [5,-3,5]
        assert 10 == solution.maxSubarraySumCircular(nums)

        nums = [3,-2,2,-3]
        assert 3 == solution.maxSubarraySumCircular(nums)
