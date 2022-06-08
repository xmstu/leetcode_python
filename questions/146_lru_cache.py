# -*- coding:utf-8 -*-


class Dlinklist(object):

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    """
    请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
    实现 LRUCache 类：
    LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
    int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

    定义头节点是最近被访问的节点, 尾节点是最久未被访问的
    也可以定义头节点是最久未被访问的节点, 尾节点是最近被访问的
    """

    def __init__(self, capacity: int):
        # lru_cache缓存的容量
        self.capacity = capacity
        # 首先要有一个字典存所有的数据
        self.cache_dict = {}
        # 还要有一个双向链表将节点按照访问的时序串起来
        dummy_head = Dlinklist(None, None)
        dummy_tail = Dlinklist(None, None)
        dummy_head.next = dummy_tail
        dummy_tail.prev = dummy_head
        self.dummy_head = dummy_head
        self.dummy_tail = dummy_tail

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        node = self.cache_dict[key] 
        self.remove_node(node)
        self.add_to_head(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        # key 在 缓存字典里面, 那么就将 key 对应的 node append 到 链表末尾
        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)
            return
        # key 不在 缓存字典里面, 那么就新建一个节点, 将node append 到链表末尾
        # 如果容量已满, 那么就删除头节点, 如果容量未满，正常添加
        new_node = Dlinklist(key, value)
        if len(self.cache_dict) < self.capacity:
            self.add_to_head(new_node)
        else:
            # 删除尾节点, 新增头节点
            self.remove_tail()
            self.add_to_head(new_node)
        self.cache_dict[key] = new_node

    def remove_node(self, node: Dlinklist):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_head(self, node: Dlinklist):
        node.prev = self.dummy_head
        node.next = self.dummy_head.next
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

    def append_tail(self, node: Dlinklist):
        node.next = self.dummy_tail
        node.prev = self.dummy_tail.prev
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node

    def remove_head(self):
        self.cache_dict.pop(self.dummy_head.next.key)
        self.dummy_head.next.next.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head.next.next
    
    def remove_tail(self):
        self.cache_dict.pop(self.dummy_tail.prev.key)
        self.dummy_tail.prev.prev.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_tail.prev.prev
    
    def link(self):
        p_node = self.dummy_head.next
        l = []
        while p_node:
            if p_node.key and p_node.value:
                l.append(str((p_node.key, p_node.value)))
            p_node = p_node.next
        
        s = " > ".join(l)
        return s


class TestLruCache(object):
    """
    pytest -s 146_lru_cache.py::TestLruCache
    """

    def test_lru_cache(self):
        obj = LRUCache(capacity=3)
        obj.put(1, 1)
        obj.put(2, 2)
        print("cache: %s" % obj.cache_dict)
        print("link: %s" % obj.link())
        assert 1 == obj.get(1)
        print("cache: %s" % obj.cache_dict)
        print("link: %s" % obj.link())
        obj.put(3, 3)
        print("cache: %s" % obj.cache_dict)
        print("link: %s" % obj.link())
        assert 2 == obj.get(2)
        obj.put(4, 4)
        print("cache: %s" % obj.cache_dict)
        print("link: %s" % obj.link())
        assert -1 == obj.get(1)
        assert 3 == obj.get(3)
        assert 4 == obj.get(4)


