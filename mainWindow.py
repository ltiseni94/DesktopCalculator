from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QVBoxLayout
from buttons import Buttons

class PyCalcUi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 235)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget)

        self.__createDisplay()
        self.__createButtons()

    def __createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def __createButtons(self):
        buttonsLayout = QGridLayout()
        self.buttons = Buttons(buttonsLayout)
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        return self.display.text()
