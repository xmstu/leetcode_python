# -*- coding:utf-8 -*-
from typing import List


class Solution:

    """
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        # 从小到大排序
        nums.sort()

        for index, num in enumerate(nums):
            # 如果前一个数和当前数相同, 跳过, 前一个数已经算过
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            target = 0 - num
            two_num_lists = self.twoSum(nums[index+1:], target)
            if not two_num_lists:
                continue
            for two_num_list in two_num_lists:
                three_num_list = [num] + two_num_list
                ans.append(three_num_list)
        
        return ans

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        ans = []
        s = set()
        for index, num in enumerate(nums):
            # 已经出现过的数, 结果已经有了, 不需要重复计算, 跳过
            if num in s:
                continue
            if target - num in map.keys():
                ans.append([target - num, num])
                s.add(num)
            else:
                map[num] = index
        
        return ans
    
    def threeSumDBPointer(self, nums: List[int]) -> List[List[int]]:
        """
        将数组从小到大排列, 用双指针进行数字的选取
        思路:
            固定三个指针: k 最小的数字, i, j 两个指针在 (k, len(nums)) 
            双指针交替向中间移动, 记录 nums[k] + nums[i] + nums[j] = 0 的组合
        1. 当 nums[k] > 0 时直接break跳出: 因为 nums[j] >= nums[i] >= nums[k] > 0, 即 3 个数字都大于 0 ，在此固定指针 k 之后不可能再找到结果了。
        2. 当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
        3. i, j 分设在数组索引 (k, len(nums))(k,len(nums)) 两端, 当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
            当s < 0时, i += 1并跳过所有重复的nums[i]:
            当s > 0时, j -= 1并跳过所有重复的nums[j]:
            当s == 0时, 记录组合[k, i, j]至res, 执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。

        """
        nums.sort()
        ans, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            # 去重
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

        return ans


class Test3sum:

    """
    pytest -s 15_3sum.py::Test3sum
    """

    def test(self):
        solution = Solution()

        nums = [-1,0,1,2,-1,-4]
        assert [[-1,-1,2], [-1,0,1]] == solution.threeSumDBPointer(nums)

        nums = []
        assert [] == solution.threeSumDBPointer(nums)

        nums = [0]
        assert [] == solution.threeSumDBPointer(nums)

        nums = [0,0,0,0]
        assert [[0,0,0]] == solution.threeSumDBPointer(nums)

        nums = [-2,0,0,2,2]
        assert [[-2,0,2]] == solution.threeSumDBPointer(nums)
