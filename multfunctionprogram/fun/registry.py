#!/usr/bin/python
#coding:utf-8
import winreg as wg
import psutil,os,time
"""
@author: GoldenKitten
@contact: GoldenKitten@163.com
@software: PyCharm
@file: registry.py
@time: 2018/9/22 13:48
"""
class Registry(object):
	def  __init__(self,path=r'SYSTEM\CurrentControlSet\Control\Keyboard Layout'):
		self.path=path
	def open_shield_windows_key(self):
		try:
			key=wg.OpenKey(
				wg.HKEY_LOCAL_MACHINE,
				self.path,
				0,wg.KEY_WRITE
			)
			wg.SetValueEx(key,'Scancode Map','',wg.REG_BINARY,
						  b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00[\xe0\x00\x00\\\xe0\x00\x00\x00\x00')
			wg.CloseKey(key)
			return True
		except Exception as e:
			print('ERROR: '+str(e.args))
			return False
		finally:
			pass
	def close_shield_windows_key(self):
		try:
			key=wg.OpenKey(
				wg.HKEY_LOCAL_MACHINE,
				self.path,
			 	0, wg.KEY_WRITE
			)
			wg.DeleteValue(key,'Scancode Map')
			wg.CloseKey(key)
			return True
		except Exception as e:
			print('ERROR: '+str(e.args[1]))
			return False
		finally:
			pass
	def check_windows_key(self):
		try:
			key=wg.OpenKey(
				wg.HKEY_LOCAL_MACHINE,
				self.path,
			 	0, wg.KEY_READ
			)
			result=wg.QueryValueEx(key,'Scancode Map')
			return True
			wg.CloseKey(key)
		except Exception as e:
			print('ERROR: '+str(e.args[1]))
			return False
		finally:
			pass
	def flush_registry(self):
		os.system(r'shutdown -r -t 0')

if __name__ == "__main__":
	r=Registry()
	r.close_shield_windows_key()
	r.check_windows_key()


