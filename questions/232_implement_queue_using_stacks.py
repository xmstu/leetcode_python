# -*- coding:utf-8 -*-


class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        # 记录的永远是入栈的队头, 如果出栈有数据, 队列的队头是出栈的栈顶, 出栈空了, 队头就变成入栈的队头
        self.front = None

    def push(self, x: int) -> None:
        # 永远是入栈写入
        if not self.input_stack:
            self.front = x
        self.input_stack.append(x)

    def pop(self) -> int:
        # 当需要 pop 的时候, 判断出栈是否为空, 是空的话将入栈的元素给出栈, 更新队头为None
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            self.front = None
        # 弹出出栈栈顶
        return self.output_stack.pop()

    def peek(self) -> int:
        # 获取队头, 如果出栈有数据, 说明进行过pop操作, 取出栈栈顶, 如果出栈没数据, 说明没有进行过pop操作, 入栈有数据, 取self.front
        if self.output_stack:
            return self.output_stack[-1]
        return self.front
        
    def empty(self) -> bool:
        if not self.input_stack and not self.output_stack:
            return True
        return False


class TestMyqueue:

    """
    pytest -s 232_implement_queue_using_stacks.py::TestMyqueue
    """

    def test(self):
        obj = MyQueue()
        obj.push(1)
        obj.push(2)
        assert 1 == obj.peek()
        assert 1 == obj.pop()
        assert obj.empty() == False

