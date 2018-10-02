#!/usr/bin/python
#coding:utf-8

"""
@author: GoldenKitten
@contact: GoldenKitten@163.com
@software: PyCharm
@file: ui_main.py
@time: 2018/9/22 13:33
"""
import sys
try:
	from ui.call_main_window import start
except ImportError as e:
	sys.path.append('.')
	from ui.call_main_window import start
if __name__ == "__main__":
	start()
