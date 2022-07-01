# -*- coding:utf-8 -*-


# 3. 打印函数调用链，打印形式不限，比如有如下函数a、b、c，执行a()，a调用了b，b调用了c，a调用了c
def c():
    return "c"

def b():
    c()
    return "b"

def a():
    b()
    c()
    return "a"



class TestMro:

	"""
	pytest -s question3.py::TestMro
	"""

	def test(self):

		value = a()
		assert value == "a"
