# -*- coding:utf-8 -*-
from typing import List

class Node:

    def __init__(self) -> None:
        self.count = 0
        self.child = {}


class Trie:

    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, word: str):
        curr = self.root
        for ch in word:
            if curr.child.get(ch) is None:
                curr.child[ch] = Node()
            curr = curr.child[ch]
        curr.count += 1


class Solution:
    """
    给定一个 m x n 二维字符网格 board 和一个单词(字符串)列表 words, 返回所有二维网格上的单词.
    单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格.
    同一个单元格内的字母在一个单词中不允许被重复使用。

    思路:
        1. 用words建立一棵字典树, 在dfs的同时, 也移动字典树上的指针, 判断搜索的路径是否在字典树上;
        2. 搜索的时候, 需要维护一个动态字符串, 在搜索路径上找到words中的单词后, 就可以记录一个答案;
        3. 优化:
            - 因为只需要在搜索路径中找到words中的单词, 所以一个单词在矩阵中有多个路径的话, 会走多余的搜索;
            - 因此可以在搜到一个单词后, 就删除字典树上的路径, 下次搜索就不用继续搜这个单词
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 第一步, 建立 Trie 树
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        Dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 开辟 visited 数组
        visited = [[False] * n for _ in range(m)]
        # 开辟动态字符串数组
        string = []
        # 开辟答案数组
        ans = set()
        def isVaild(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def dfs(board, x: int, y: int, curr: Node):
            
            ch = board[x][y]
            # 如果在字典树上没找到这个字符, 说明word不在上面, 直接返回, 该路径不用继续找下去了
            if curr.child.get(ch) is None:
                return
            string.append(ch)
            next_node = curr.child[ch]
            if next_node.count > 0:
                ans.add("".join(string))

            for dx, dy in Dir:
                nx, ny = x + dx, y + dy
                if not isVaild(nx, ny):
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                dfs(board, nx, ny, next_node)
                visited[nx][ny] = False
            string.pop()

        # 枚举每个起点
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                dfs(board, i, j, trie.root)
                visited[i][j] = False

        ans = list(ans) 
        return ans


class Solution2:
    """
    优化:
        - 因为只需要在搜索路径中找到words中的单词, 所以一个单词在矩阵中有多个路径的话, 会走多余的搜索;
        - 因此可以在搜到一个单词后, 就删除字典树上的路径, 下次搜索就不用继续搜这个单词;
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 第一步, 建立 Trie 树
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        Dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 开辟 visited 数组
        visited = [[False] * n for _ in range(m)]
        # 开辟动态字符串数组
        string = []
        # 开辟答案数组
        ans = set()
        def isVaild(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def dfs(board, x: int, y: int, curr: Node):
            if curr is None:
                return
            ch = board[x][y]
            # 如果在字典树上没找到这个字符, 说明word不在上面, 直接返回, 该路径不用继续找下去了
            if curr.child.get(ch) is None:
                return
            string.append(ch)
            next_node = curr.child[ch]
            if next_node.count > 0:
                ans.add("".join(string))
            
            # 判断 next_node 的 child 字典是否为空, 是空的话就删除这个节点
            if not next_node.child:
                curr.child.pop(ch)
                del next_node
                string.pop()
                return

            for dx, dy in Dir:
                nx, ny = x + dx, y + dy
                if not isVaild(nx, ny):
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                dfs(board, nx, ny, next_node)
                visited[nx][ny] = False
            string.pop()

        # 枚举每个起点
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                dfs(board, i, j, trie.root)
                visited[i][j] = False

        ans = list(ans) 
        return ans


class TestFindWords:

    """
    pytest -s 212_word_search_2.py::TestFindWords
    """

    def test(self):
        solution = Solution2()

        board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ]
        words = ["oath","pea","eat","rain"]
        assert ["oath", "eat"] == solution.findWords(board, words)

        board = [["a","b"],["c","d"]]; words = ["abcb"]
        assert [] == solution.findWords(board, words)
