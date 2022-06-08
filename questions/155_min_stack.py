# -*- coding:utf-8 -*-
from queue import LifoQueue


class MinStack:

    def __init__(self):
        self.stack = LifoQueue()
        self.preMinStack = LifoQueue()

    def push(self, val: int) -> None:
        self.stack.put(val)
        if self.preMinStack.empty():
            self.preMinStack.put(val)
        else:
            self.preMinStack.put(min(self.preMinStack.queue[-1], val))

    def pop(self) -> None:
        self.stack.get()
        self.preMinStack.get()

    def top(self) -> int:
        return self.stack.queue[-1]
        
    def getMin(self) -> int:
        return self.preMinStack.queue[-1]


class MinStack2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = -1

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_value = x
        else:
            diff = x-self.min_value
            self.stack.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value
                self.min_value = top - diff
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value if self.stack else -1


class TestMinStack:
    """
    pytest -s 155_min_stack.py::TestMinStack
    """

    def test(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        assert -3 == obj.getMin()
        obj.pop()
        obj.pop()
        assert -2 == obj.getMin()

        obj2 = MinStack2()
        obj2.push(-2)
        print("obj2.minValue: %s" % obj2.min_value)
        obj2.push(0)
        print("obj2.minValue: %s" % obj2.min_value)
        obj2.push(-3)
        print("obj2.minValue: %s" % obj2.min_value)
        print("obj2.stack: %s" % obj2.stack)
        assert -3 == obj2.getMin()
        obj2.pop()
        obj2.pop()
        assert -2 == obj2.getMin()
