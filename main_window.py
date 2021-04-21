import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel('Hello World!'))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.file = self.menuBar().addMenu('File')
        self.modify = self.menuBar().addMenu('Modify')
        self.view = self.menuBar().addMenu('View')
        self.settings = self.menuBar().addMenu('Settings')
        self.file.addAction('Exit', self.close)
        self.modify.addAction('Trash', self.close)
        self.view.addAction('Trash', self.close)
        self.settings.addAction('Trash', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
