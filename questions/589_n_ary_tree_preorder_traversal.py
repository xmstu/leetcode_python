# -*- coding:utf-8 -*-
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        seq = []
        def dfs(root: Node):
            if root is None:
                return
            seq.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return seq
    
    def preorder_stack(self, root: Node) -> List[int]:
        seq = []
        if root is None:
            return seq
        stack = [root]

        while stack:
            node = stack.pop()
            seq.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        
        return seq



class TestPreorder:

    """
    pytest -s 589_n_ary_tree_preorder_traversal.py::TestPreorder
    """

    def test(self):
        solution = Solution()

        root = Node(val=1, children=[
            Node(val=3, children=[Node(5, children=[]), Node(6, children=[])]),
            Node(val=2, children=[]),
            Node(val=4, children=[]),
        ])
        assert [1,3,5,6,2,4] == solution.preorder(root)
        assert [1,3,5,6,2,4] == solution.preorder_stack(root)
