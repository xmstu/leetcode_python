# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.cap = 0
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.addToHead(value) 
        self.cap += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.appendTail(value)
        self.cap += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.removeHead()
        self.cap -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.removeTail() 
        self.cap -= 1
        return True
    
    def addToHead(self, value: int):
        node = ListNode(value)
        node.prev = self.dummy_head
        node.next = self.dummy_head.next
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

    def appendTail(self, value: int):
        node = ListNode(value)
        node.next = self.dummy_tail
        node.prev = self.dummy_tail.prev
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node

    def removeHead(self):
        self.dummy_head.next.next.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head.next.next

    def removeTail(self):
        self.dummy_tail.prev.prev.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_tail.prev.prev

    def getFront(self) -> int:
        return self.dummy_head.next.val if self.cap > 0 else -1

    def getRear(self) -> int:
        return self.dummy_tail.prev.val if self.cap > 0 else -1


    def isEmpty(self) -> bool:
        return True if self.cap == 0 else False

    def isFull(self) -> bool:
        return True if self.cap == self.k else False


class TestCircularDeque:

    """
    pytest -s 641_design_circular_deque.py::TestCircularDeque
    """

    def test(self):
        obj = MyCircularDeque(3)
        obj.insertLast(1)
        obj.insertLast(2)
        obj.insertFront(3)
        assert False == obj.insertFront(4)
        assert 2 == obj.getRear()
        assert True == obj.isFull()
        obj.deleteLast()
        obj.insertFront(4)
        assert 4 == obj.getFront()
        
        