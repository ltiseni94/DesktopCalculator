#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
from controller import Controller
from mainWindow import PyCalcUi
import sys

__version__ = '0.1'
__author__ = 'luct94'

# Warning: It is not a useless project :)

def main():
    pycalc = QApplication(sys.argv)
    pyCalcWindow = PyCalcUi()
    controler = Controller(pyCalcWindow)
    pyCalcWindow.show()
    sys.exit(pycalc.exec_())

if __name__ == '__main__': main()
