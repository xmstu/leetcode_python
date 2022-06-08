# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = defaultdict(list)
        for s in strs:
            list_s = list(s)            
            list_s.sort()
            sort_s = "".join(list_s)
            group_map[sort_s].append(s)
        
        ans = list(group_map.values())
        return ans
    
    def groupAnagramsTuple(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        
        return list(mp.values())


class TestGroupAnagrams:
    """
    pytest -s 49_group_anagrams.py::TestGroupAnagrams
    """

    def test(self):
        solution = Solution()

        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        assert [["bat"],["nat","tan"],["ate","eat","tea"]] == solution.groupAnagrams(strs)

        strs = [""]
        assert [[""]] == solution.groupAnagrams(strs)

        strs = ["a"]
        assert [["a"]] == solution.groupAnagrams(strs)

