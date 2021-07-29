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
