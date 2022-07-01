# -*- coding:utf-8 -*-
""" 
题目: 2. 根据设定的期待输出 (x) 进行 (N) 次重试
"""


def retry(expect_output, retry_count):

    def wrapper(func):
        def inner(*args, **kwargs):
            output = func(*args, **kwargs)
            if output == expect_output:
                return output
            else:
                retry_cnt = 0
                for _ in range(retry_count):
                    retry_cnt += 1
                    output = func(*args, **kwargs)
                    print("retry: %s, output: %s" % (retry_cnt, output))
                    if output == expect_output:
                        return output
                return 
        return inner
    
    return wrapper


class TestRetry:

    """
    pytest -s jiukun_question2_retry.py::TestRetry
    """

    def test(self):
        import random

        @retry(expect_output=3, retry_count=100)
        def rand():
            value = random.randint(1, 10)
            return value
        
        value = rand()
        assert value == 3
