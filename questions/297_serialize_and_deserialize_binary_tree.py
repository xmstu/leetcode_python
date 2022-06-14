# -*- coding:utf-8 -*-
from collections import deque
from typing import List


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        seq = []
        self.dfs(seq, root)
        return ",".join(seq)

    def dfs(self, seq: List, root: TreeNode):
        if root is None:
            seq.append("null")
            return
        
        seq.append(str(root.val))
        self.dfs(seq, root.left)
        self.dfs(seq, root.right)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.seq = data.split(",")
        self.cur = 0
        return self.restore()
    
    def restore(self):
        if self.seq[self.cur] == "null":
            self.cur += 1
            return None
        
        root = TreeNode(int(self.seq[self.cur]))
        self.cur += 1
        root.left = self.restore()
        root.right = self.restore()
        return root
    

class CodecBfs:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque()
        q.appendleft(root)
        res = ''
        while q:
            node = q.pop()
            if node != None:
                res += str(node.val) + ','
                q.appendleft(node.left)
                q.appendleft(node.right)
            else:
                res += 'null,'
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q = deque()
        q.appendleft(root)
        cursor = 1
        while q:
            node = q.pop()
            left_val, right_val = data[cursor], data[cursor + 1]
            if left_val != 'null':
                node.left = TreeNode(int(left_val))
                q.appendleft(node.left)
            if right_val != 'null':
                node.right = TreeNode(int(right_val))
                q.appendleft(node.right)
            cursor += 2
        return root

        
class TestCodec:

    """
    pytest -s 297_serialize_and_deserialize_binary_tree.py::TestCodec
    """

    def test(self):
        codec = Codec()

        root = TreeNode(
            val=1,
            left=TreeNode(val=2),
            right=TreeNode(val=3,
                           left=TreeNode(4),
                           right=TreeNode(5),
                           )
            )
        tree_str = codec.serialize(root)
        assert tree_str == "1,2,null,null,3,4,null,null,5,null,null"

        new_root = codec.deserialize(tree_str)
        assert new_root.val == 1
        assert new_root.left.val == 2
        assert new_root.right.val == 3
        assert new_root.right.left.val == 4
        assert new_root.right.right.val == 5

        codec_bfs = CodecBfs()

        tree_str = codec_bfs.serialize(root)

        new_root = codec_bfs.deserialize(tree_str)
        assert new_root.val == 1
        assert new_root.left.val == 2
        assert new_root.right.val == 3
        assert new_root.right.left.val == 4
        assert new_root.right.right.val == 5

