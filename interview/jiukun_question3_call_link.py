# -*- coding:utf-8 -*-

"""
1. 利用全局变量 PARENT_FUNC 记录调用的父亲函数名, 再用 call_list 记录调用链;
2. 关键点: 回溯, 在调用完 func 后, 记得还原父亲函数名;
3. 美中不足的地方: 用了全局变量, 整个代码不是很清爽;
"""

call_list = []
PARENT_FUNC = None


def call_deco(func):

	def inner(*args, **kwargs):
		global PARENT_FUNC
		last_parent = PARENT_FUNC
		if PARENT_FUNC and PARENT_FUNC != func.__name__:
			call_list.append("%s -> %s" % (PARENT_FUNC, func.__name__))
		PARENT_FUNC = func.__name__
		output = func(*args, **kwargs)
		# 回溯, 还原现场
		PARENT_FUNC = last_parent

		return output
	
	return inner


# 3. 打印函数调用链，打印形式不限，比如有如下函数a、b、c，执行a()，a调用了b，b调用了c，a调用了c
@call_deco
def c():
    return "c"

@call_deco
def b():
    c()
    return "b"

@call_deco
def a():
    b()
    c()
    return "a"


class TestCallLink:

	"""
	pytest -s jiukun_question3_call_link.py::TestCallLink
	"""

	def test(self):

		value = a()
		print("value: %s" % value)
		print("call_list: %s" % call_list)
		print("PARENT_FUNC: %s" % PARENT_FUNC)
		assert ["a -> b", "b -> c", "a -> c"] == call_list
