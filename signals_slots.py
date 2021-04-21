import sys
import functools
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting(lb, name):
    if lb.text():
        lb.setText('')
    else:
        lb.setText(f'Hello {name}!')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

msg = QLabel('')
btn = QPushButton('Greet')
#btn.clicked.connect(lambda: msg.setText('') if msg.text() else msg.setText(f'Hello Luca'))
btn.clicked.connect(functools.partial(greeting, lb=msg, name='Luca'))

layout.addWidget(btn)
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
