#!/usr/bin/python
#coding:utf-8

"""
@author: GoldenKitten
@contact: GoldenKitten@163.com
@software: PyCharm
@file: call_main_window.py
@time: 2018/10/1 14:35
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QDesktopWidget
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from ui.ui_main import Ui_MainWindow
from fun import Registry
class MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.setupUi(self)
		self.center()
		self.registry=Registry()
		_translate = QtCore.QCoreApplication.translate
		if self.registry.check_windows_key():
			self.pushButton.setText(_translate("MainWindow", "关闭屏蔽Windows键"))
			self.pushButton.clicked.connect(lambda :self.btn(True))
		else:
			self.pushButton.setText(_translate("MainWindow", "开启屏蔽Windows键"))
			self.pushButton.clicked.connect(lambda: self.btn(False))
		self.information('提示', '本程序运行需要管理员权限并且在使用过程中会重启电脑')

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def information(self,title,content):
		qm = QMessageBox()
		qm.information(self,title,content)
		qm.setWindowModality(Qt.WindowModal)
	def btn(self,state):
		if state:
			if self.registry.close_shield_windows_key():
				self.registry.flush_registry()
			else:
				self.information('提示','请以管理员身份运行本程序')
				sys.exit()
		else:
			if self.registry.open_shield_windows_key():
				self.registry.flush_registry()
			else:
				self.information('提示','请以管理员身份运行本程序')
				sys.exit()

def start():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
if __name__ == "__main__":
	start()
