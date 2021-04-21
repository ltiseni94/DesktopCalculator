import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QSpinBox


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')
layout = QFormLayout()
layout.addRow('Name:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QSpinBox())
layout.addRow('Hobbies:', QComboBox())
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
