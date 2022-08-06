# -*- coding:utf-8 -*-
from collections import defaultdict, deque
from typing import List
from heapq import heappush, heappop


class Solution:
    """
    在一个 2 x 3 的板上(board) 有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换.
    最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
    给出一个谜板的初始状态 board, 返回最少可以通过多少次移动解开谜板, 如果不能解开谜板, 则返回 -1 。
    """
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def zip_board(board: List[List[int]]) -> str:
            res = ''
            for i in range(2):
                for j in range(3):
                    res += str(board[i][j])
            
            return res
        
        def findZeroIndex(s: str) -> int:
            for index, ch in enumerate(s):
                if ch == '0':
                    return index
            return -1
        
        def expand(s: str, pos: int, other: int):
            ns = list(s)
            ns[pos], ns[other] = ns[other], ns[pos]
            ns = "".join(ns)
            if ns in depth:
                return
            depth[ns] = depth[s] + 1
            q.appendleft(ns)
        
        start = zip_board(board)
        target = zip_board([[1,2,3], [4,5,0]])
        q = deque()
        q.appendleft(start)
        depth = defaultdict(int)
        depth[start] = 0
        
        while q:
            s = q.pop()
            pos = findZeroIndex(s)
            if pos >= 3:
                expand(s, pos, pos - 3)
            if pos <= 2:
                expand(s, pos, pos + 3)
            if pos % 3 != 0:
                expand(s, pos, pos - 1)
            if pos % 3 != 2:
                expand(s, pos, pos + 1)
            
            if target in depth:
                return depth[target]
        
        return -1


class Pair:

    def __init__(self, evaluate_value, s) -> None:
        self.evaluate_value = evaluate_value
        self.s = s
    
    def __lt__(self, other):
        return self.evaluate_value <= other.evaluate_value


class Solution2:
    """
    在一个 2 x 3 的板上(board) 有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换.
    最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
    给出一个谜板的初始状态 board, 返回最少可以通过多少次移动解开谜板, 如果不能解开谜板, 则返回 -1 。
    """
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        思路: A*算法, 每次加上代价估计, 用小根堆维护可能是代价最小的堆顶, 取出堆顶进行 bfs
        """

        def zip_board(board: List[List[int]]) -> str:
            res = ''
            for i in range(2):
                for j in range(3):
                    res += str(board[i][j])
            
            return res
        
        def findZeroIndex(s: str) -> int:
            for index, ch in enumerate(s):
                if ch == '0':
                    return index
            return -1
        
        def expand(s: str, pos: int, other: int):
            ns = list(s)
            ns[pos], ns[other] = ns[other], ns[pos]
            ns = "".join(ns)
            if ns in depth:
                return
            depth[ns] = depth[s] + 1
            # 当前步数 加上 估算距离
            heappush(q, Pair(depth[ns] + evaluate(ns), ns))
        
        def evaluate(s: str):
            """
            估价函数, 计算当前字符串和target的距离之差, 距离是 s 每个字符到达目标字符串 target 中每个对应字符坐标的绝对值之差的和
            """
            now = [0] * 6
            for i in range(6):
                if s[i] != '0':
                    now[int(s[i])] = i
            
            target = [0, 0, 1, 2, 3, 4]
            ans = 0
            for digit in range(1, 6):
                nowx = now[digit] // 3
                nowy = now[digit] % 3
                targetx = target[digit] // 3
                targety = target[digit] // 3
                ans += abs(nowx - targetx) + abs(nowy - targety)

            return ans

        
        start = zip_board(board)
        target = zip_board([[1,2,3], [4,5,0]])
        # 初始化最小堆, 最开始是 0 步 加上 估价距离
        q = []
        heappush(q, Pair(0 + evaluate(start), start))
        depth = defaultdict(int)
        depth[start] = 0
        
        while q:
            s = q[0].s
            heappop(q)
            pos = findZeroIndex(s)
            if pos >= 3:
                expand(s, pos, pos - 3)
            if pos <= 2:
                expand(s, pos, pos + 3)
            if pos % 3 != 0:
                expand(s, pos, pos - 1)
            if pos % 3 != 2:
                expand(s, pos, pos + 1)
            
            if target in depth:
                return depth[target]
        
        return -1


class TestSlidingPuzzle:

    """
    pytest -s 773_sliding_puzzle.py::TestSlidingPuzzle
    """

    def test(self):
        solution = Solution2()

        board = [[1,2,3],[4,0,5]]
        assert 1 == solution.slidingPuzzle(board)

        board = [[1,2,3],[5,4,0]]
        assert -1 == solution.slidingPuzzle(board)

        board = [[4,1,2],[5,0,3]]
        assert 5 == solution.slidingPuzzle(board)

        board = [[4,3,5],[2,1,0]]
        assert 8 == solution.slidingPuzzle(board)
