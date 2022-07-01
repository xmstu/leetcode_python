# -*- coding:utf-8 -*-
import time
import hashlib


def hash_key(*args, **kwargs):
    value_list = []
    for arg in args:
        value_list.append(str(arg))
    for key, value in kwargs.items():
        value_list.append(str(value))
    
    s = "".join(value_list)
    key = hashlib.md5(s.encode()).hexdigest()
    return key


# 1. 缓存函数最近(N)次的输入和输出，可控制每个缓存存在的时间为(M)秒，命中缓存则直接返回结果
def ttlcache(max_size, ttl):

    cache_map = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            print("fuck cache map: %s" % cache_map)
            key = hash_key(*args, **kwargs)
            value_map = cache_map.get(key)
            if value_map:
                if value_map["expire_time"] >= time.time():
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
                    if value_map["expire_time"] < time.time():
                        print("delete expire key: %s" % cache_key)
                        pop_keys.append(cache_key)
                for pop_key in pop_keys:
                    cache_map.pop(pop_key)
            # 缓存经过删除, 让出了空位, 就将缓存加进去
            if len(cache_map) < max_size:
                cache_map[key] = {"output": output, "expire_time": time.time() + ttl}
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
