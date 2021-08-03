import sys, os, random, win32clipboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(300, 300, 580, 400)
        self.setWindowTitle("#Tag Generator")

        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.setWindowIcon(QtGui.QIcon("icon.ico"))

        self.front_element = QtGui.QFont()
        self.front_element.setPointSize(16)
        self.front_element.setBold(True)
        self.front_element.setWeight(75)

        self.long_tags = QtGui.QFont()
        self.long_tags.setPointSize(12)
        self.long_tags.setBold(True)
        self.long_tags.setWeight(75)

        self.initUI()

        self.tag_list = self.read_tags()
        self.lcd_tagCount.display(int(len(self.tag_list)))

    def initUI(self):
        self.button_add = QtWidgets.QPushButton(self)
        self.button_add.setObjectName("button_add")
        self.button_add.setGeometry(QtCore.QRect(10, 10, 111, 81))
