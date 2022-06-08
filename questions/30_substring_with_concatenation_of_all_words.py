# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict


class Solution:
    """
    给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
    注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 每个单词的长度是一致的
        word_len = len(words[0])
        # 所有单词加起来的长度
        tot = word_len * len(words)
        ans = []

        # 构造单词映射字典
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1
        
        i = 0
        # 每个子串的长度都是 单词个数 乘以 单个单词长度
        while i + tot <= len(s):
            # 判断子字符串构造的单词 hash 字典 和 传进来的单词映射字典是否一样, 是一样的就说明, 该子串完全由单词构成
            is_vaild, step = self.valid(s[i:i+tot], word_len, word_map)
            # 如果是有效的, 每次 i 移动 一个单词的长度, 否则移动一个字符长度
            if is_vaild:
                ans.append(i)
            i += step

        return ans
    
    def valid(self, sub_str, word_len, word_map):
        split_word_map = defaultdict(int)
        # 按照 单个 单词的长度切割子串, 构造子串的切割单词映射字典
        is_vaild = False
        step = 1
        i = 0
        while i < len(sub_str):
            split_word = sub_str[i:i+word_len]
            # 切割的单词不在 word_map 中, 就可以直接break, 不用继续构造切割单词字典, 步长为1
            if split_word in word_map:
                split_word_map[split_word] += 1
                i += word_len
            else:
                break
        # 全匹配
        if split_word_map == word_map:
            is_vaild = True 
            # 像 aa 这种单词, 都由同一个字符构成的, 每次只能移动一位, 不然移动 2 位, 答案不全
            step = word_len if len(word_map) > 1 else step
        return is_vaild, step


class TestFindSubString:

    """
    pytest -s 30_substring_with_concatenation_of_all_words.py::TestFindSubString
    """

    def test(self):
        solution = Solution()

        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        assert [0, 9] == solution.findSubstring(s, words)

        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        assert [] == solution.findSubstring(s, words)

        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        assert [6,9,12] == solution.findSubstring(s, words)

        s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        words = ["fooo","barr","wing","ding","wing"]
        assert [13] == solution.findSubstring(s, words)

        s = "aaaaaaaaaaaaaa"
        words = ["aa","aa"]
        assert [0,1,2,3,4,5,6,7,8,9,10] == solution.findSubstring(s, words)


