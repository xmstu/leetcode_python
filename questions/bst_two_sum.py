# -*- coding:utf-8 -*-
from typing import List


class Node:

    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class TreePointer:

    def __init__(self, cur: Node):
        self.stack: List[Node] = []
        self.cur = cur


def createCompleteBst(array: List[int], left: int, right: int) -> Node:
    if right == -1:
        right = len(array)
    if right <= left:
        return None
    
    level = 1
    length = right - left
    while 2 ** level - 1 <= length:
        level += 1

    lastLevelNodes = length - (2 ** (level - 1) - 1)
    lastLevelMaxNodes = 2 ** (level - 1)
    lastLevelLeft = min(lastLevelNodes, lastLevelMaxNodes / 2)
    leftNodes = (2 ** (level - 2) - 1) + lastLevelLeft

    pivitIndex = int(left + leftNodes)
    print(f"pivitIndex: {pivitIndex}")
    root = Node(val=array[pivitIndex])
    root.left = createCompleteBst(array, left, pivitIndex)
    root.right = createCompleteBst(array, pivitIndex + 1, right)
    
    return root


def display(root: Node, level: int):
    tab_s = "".join(["\t" for _ in range(level)])
    print(tab_s + str(root.val))
    if root.left != None:
        display(root.left, level + 1)
    if root.right != None:
        display(root.right, level + 1)


def toLeftMost(pointer: TreePointer):
    cur = pointer.cur
    while cur != None:
        pointer.stack.append(cur)
        cur = cur.left
    pointer.cur = pointer.stack.pop()
    return pointer.cur.val

def toRightMost(pointer: TreePointer):
    cur = pointer.cur
    while cur != None:
        pointer.stack.append(cur)
        cur = cur.right
    pointer.cur = pointer.stack.pop()
    return pointer.cur.val

def moveLeft(pointer: TreePointer):
    cur = pointer.cur
    if cur.left != None:
        pointer.cur = cur.left
        return toRightMost(pointer)
    else:
        pointer.cur = pointer.stack.pop()
        return pointer.cur.val

def moveRight(pointer: TreePointer):
    cur = pointer.cur
    if cur.right != None:
        pointer.cur = cur.right
        return toLeftMost(pointer)
    else:
        pointer.cur = pointer.stack.pop()
        return pointer.cur.val


class Solution:

    """
    题目要求: 1. 给定一个有序数组, 构建一棵二叉搜索树; 2. 给定一个整数, 判断这个整数是否为这棵搜索树上其中的两数之和; 
    """

    @staticmethod
    def bstTwoSum(root: Node, target: int):
        leftPointer = TreePointer(root)
        leftValue = toLeftMost(leftPointer)

        rightPointer = TreePointer(root)
        rightValue = toRightMost(rightPointer)

        while target != leftValue + rightValue:
            print(f"leftValue: {leftValue}, rightValue: {rightValue}")

            # 如果 target 大于 两数之和, 左指针右移, 否则, 右指针左移
            if target > leftValue + rightValue:
                leftValue = moveRight(leftPointer)
            else:
                rightValue = moveLeft(rightPointer)
            
            if leftPointer.cur == rightPointer.cur:
                return False
        
        return True


class TestBstTwoSum:

    """
    pytest -s bst_two_sum.py::TestBstTwoSum
    """

    def test(self):
        solution = Solution()

        array = [1, 3, 8, 11, 16, 21, 28, 39, 40, 41, 46, 53, 64]
        root = createCompleteBst(array=array, left=0, right=-1)
        print("\n")
        display(root=root, level=0)
        assert True == solution.bstTwoSum(root=root, target=51)
        print("\n")
        assert False == solution.bstTwoSum(root=root, target=58)
