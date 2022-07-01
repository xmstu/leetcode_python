# -*- coding:utf-8 -*-
import time
import hashlib

"""
题目: 1. 缓存函数最近(N)次的输入和输出，可控制每个缓存存在的时间为(M)秒，命中缓存则直接返回结果

思路:
    1. 将调用函数的参数按照一定的规则排序好, 将参数值字符串化, 经过hash得到hash的key值;
    2. 用 cache_map 记录该参数的函数输出值, key是参数hash_key, value是 字典 {"output": xxx, "expire_time": xxx};
    3. expire_time是在记录缓存的时候确定下来的, 是函数调用的当前时间加上传入的 ttl, 从而在后续过程中删除缓存;
"""


def hash_key(*args, **kwargs):
    value_list = []
    for arg in args:
        value_list.append(str(arg))
    
    for key, value in kwargs.items():
        value_list.append(str(key) + str(value))
    
    value_list.sort()
    
    s = "".join(value_list)
    key = hashlib.md5(s.encode()).hexdigest()
    return key


def ttlcache(max_size, ttl):

    cache_map = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            now = time.time()
            print("fuck cache map: %s" % cache_map)
            key = hash_key(*args, **kwargs)
            value_map = cache_map.get(key)
            if value_map:
                if value_map["expire_time"] >= now:
                    print("use cache, output: %s" % value_map["output"])
                    return value_map["output"]
                # 过期删除缓存
                else:
                    print("delete one expire cache, output: %s" % value_map["output"])
                    cache_map.pop(key)

            output = func(*args, **kwargs)
            print("not use cache, output: %s" % output)
            if len(cache_map) >= max_size:
                # 将所有过期的缓存全部删除
                pop_keys = []
                for cache_key, value_map in cache_map.items():
                    if value_map["expire_time"] < now:
                        print("delete expire key: %s" % cache_key)
                        pop_keys.append(cache_key)
                for pop_key in pop_keys:
                    cache_map.pop(pop_key)
            # 缓存经过删除, 让出了空位, 就将缓存加进去
            if len(cache_map) < max_size:
                cache_map[key] = {"output": output, "expire_time": now + ttl}
            return output
        return inner
    
    return wrapper



class TestTTLCache:

    """
    pytest -s jiukun_question1_ttlcache.py::TestTTLCache
    """

    def test(self):

        
        @ttlcache(max_size=1, ttl=3)
        def pow(x, y):
            return x ** y
        
        assert 9 == pow(3, 2)
        assert 16 == pow(4, 2)
        assert 9 == pow(3, 2)
        assert 16 == pow(4, 2)
        print("sleep times")
        time.sleep(3)
        assert 16 == pow(4, 2)
        assert 9 == pow(3, 2)
        assert 16 == pow(4, 2)
