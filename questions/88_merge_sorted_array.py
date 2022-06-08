from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        result = []
        while i < m or j < n:
            if j >= n or (i < m and nums1[i] < nums2[j]):
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        for i, _ in enumerate(nums1):
            nums1[i] = result[i]
        print("fuck merge use extra array nums1: %s" % nums1)
        return
    
    def merge_in_place(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        倒着进行合并, 这样nums1的空间是足够的, 正着遍历可能会用nums2里的值覆盖掉nums1的值, 所以最好倒着合并
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        for k in range(m + n -1, -1, -1):
            # 倒着合并, 哪个大要哪个, 数组1遍历到了头, 就到塞数组2剩下的数字即可
            if (j < 0 or (i >= 0 and nums1[i] >= nums2[j])):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        print("fuck merge in place nums1: %s" % nums1)
    

class TestMergeSortedArray(object):

    """
    执行命令跑单测:  pytest -s 88_merge_sorted_array.py::TestMergeSortedArray
    """

    def test_move_zero(self):
        solution = Solution()

        nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1,2,2,3,5,6]

        nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
        solution.merge_in_place(nums1, m, nums2, n)
        assert nums1 == [1,2,2,3,5,6]

        nums1, m, nums2, n = [1], 1, [], 0
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1]

        nums1, m, nums2, n = [0], 0, [1], 1
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1]



