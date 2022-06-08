# -*- coding:utf-8 -*-
from collections import deque


class MyStack:

    def __init__(self):
        self.input_queue = deque()
        self.output_queue = deque()

    def push(self, x: int) -> None:
        """
        通过不断交换 入队 和 出队, 从而实现栈的后进先出
        push: 1, 2, 3

        push(1)
        in: [1], out: [] => in: [], out: [1]

        push(2)
        in: [2], out: [1] => in: [1,2], out: [] => in: [], out: [1,2]

        push(3)
        in: [3], out: [1,2] => in: [1,2,3], out: [] => in: [], out: [1,2,3]
        """
        self.input_queue.appendleft(x)
        while self.output_queue:
            self.input_queue.appendleft(self.output_queue.pop())
        self.input_queue, self.output_queue = self.output_queue, self.input_queue

    def pop(self) -> int:
        return self.output_queue.pop()

    def top(self) -> int:
        return self.output_queue[-1]

    def empty(self) -> bool:
        return not self.output_queue


class MyStackSingleQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        q: [3,2,1]
        push(4)
            q: [3,2,1,4]
            q: popleft() [2,1,4] 3 => append(3) [2,1,4,3]
            q: popleft() [1,4,3] 2 => append(2) [1,4,3,2]
            q: popleft() [4,3,2] 1 => append(1) [4,3,2,1]
        """
        # 单个队列实现栈, 每次都是 push 新元素, 就是从队头 popleft n 个元素再加入到队尾
        # 队头就是栈顶, 队尾就是栈底
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


class TestMyStack:

    """
    pytest -s 225_implement_stack_using_queues.py::TestMyStack
    """

    def test(self):
        obj = MyStack()
        obj.push(1)
        obj.push(2)
        obj.push(3)
        print("input queue: %s, output queue: %s" % (obj.input_queue, obj.output_queue))
        assert 3 == obj.pop()
        obj.push(4)
        print("input queue: %s, output queue: %s" % (obj.input_queue, obj.output_queue))
        assert 4 == obj.top()
        assert False == obj.empty()


