# -*- coding:utf-8 -*-

class Node:

    def __init__(self) -> None:
        self.count = 0
        self.child = [None] * 26

class Trie:
    """
    Trie (发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
    Trie 树也叫字典树
    请你实现 Trie 类：
        Trie() 初始化前缀树对象。
        void insert(String word) 向前缀树中插入字符串 word 。
        boolean search(String word) 如果字符串 word 在前缀树中，返回 true (即，在检索之前已经插入)；否则，返回 false 。
        boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

    使用数组记录子节点, 在对应字符的下标下记录新节点
    """

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.find(word, isInsert=True, isPrefix=False)

    def search(self, word: str) -> bool:
        return self.find(word, isInsert=False, isPrefix=False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, isInsert=False, isPrefix=True)

    def find(self, s, isInsert: bool, isPrefix: bool) -> bool:
        curr = self.root
        for ch in s:
            if curr.child[ord(ch) - ord("a")] is None:
                if isInsert:
                    curr.child[ord(ch) - ord("a")] = Node()
                else:
                    return False
            curr = curr.child[ord(ch) - ord("a")]
        if isInsert:
            curr.count += 1
        if isPrefix:
            return True
        return curr.count > 0


class TrieArray:

    def __init__(self):
        self.root = [0, [None] * 26]

    def insert(self, word: str) -> None:
        self.find(word, isInsert=True, isPrefix=False)

    def search(self, word: str) -> bool:
        return self.find(word, isInsert=False, isPrefix=False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, isInsert=False, isPrefix=True)

    def find(self, s, isInsert: bool, isPrefix: bool) -> bool:
        curr = self.root
        for ch in s:
            if curr[1][ord(ch) - ord("a")] is None:
                if isInsert:
                    curr[1][ord(ch) - ord("a")] = [0, [None] * 26]
                else:
                    return False
            curr = curr[1][ord(ch) - ord("a")]
        if isInsert:
            curr[0] += 1
        if isPrefix:
            return True
        return curr[0] > 0
        

class NodeHashMap:

    def __init__(self) -> None:
        self.count = 0
        self.child = {}


class TrieHashMap:
    """
    使用字典存子节点 
    """
    def __init__(self):
        self.root = NodeHashMap()

    def insert(self, word: str) -> None:
        self.find(word, isInsert=True, isPrefix=False)

    def search(self, word: str) -> bool:
        return self.find(word, isInsert=False, isPrefix=False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, isInsert=False, isPrefix=True)

    def find(self, s, isInsert: bool, isPrefix: bool) -> bool:
        curr = self.root
        for ch in s:
            if curr.child.get(ch) is None:
                if isInsert:
                    curr.child[ch] = NodeHashMap()
                else:
                    return False
            curr = curr.child[ch]
        if isInsert:
            curr.count += 1
        if isPrefix:
            return True
        return curr.count > 0


class TrieHashMap2:
    """
    使用字典存子节点 
    """
    def __init__(self):
        self.root = [0, {}]

    def insert(self, word: str) -> None:
        self.find(word, isInsert=True, isPrefix=False)

    def search(self, word: str) -> bool:
        return self.find(word, isInsert=False, isPrefix=False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, isInsert=False, isPrefix=True)

    def find(self, s, isInsert: bool, isPrefix: bool) -> bool:
        curr = self.root
        for ch in s:
            if curr[1].get(ch) is None:
                if isInsert:
                    curr[1][ch] = [0, {}]
                else:
                    return False
            curr = curr[1][ch]
        if isInsert:
            curr[0] += 1
        if isPrefix:
            return True
        return curr[0] > 0



class TestTrie:

    """
    pytest -s 208_implement_trie.py::TestTrie
    """

    def test(self):
        trie = TrieHashMap2()

        trie.insert("apple")
        assert True == trie.search("apple")
        assert False == trie.search("app")
        assert True == trie.startsWith("app")
        trie.insert("app")
        assert True == trie.search("app")

