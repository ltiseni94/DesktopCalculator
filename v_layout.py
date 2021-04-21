import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Vertical Layout')

layout = QVBoxLayout()
layout.addWidget((QPushButton('Top')))
layout.addWidget((QPushButton('Center')))
layout.addWidget((QPushButton('Right')))
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
