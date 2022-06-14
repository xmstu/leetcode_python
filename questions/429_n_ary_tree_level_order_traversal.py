# -*- coding:utf-8 -*-
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque()
        seq = []
        if root is None:
            return seq
        q.appendleft((root, 0))
        while q:
            pair = q.pop()
            node, depth = pair[0], pair[1]
            if depth >= len(seq):
                seq.append([])
            seq[depth].append(node.val)
            for child in node.children:
                q.appendleft((child, depth + 1))
        
        return seq
        
