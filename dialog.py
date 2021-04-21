import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlglayout = QVBoxLayout()
        formlayout = QFormLayout()
        formlayout.addRow('Name:', QLineEdit())
        formlayout.addRow('Age:', QLineEdit())
        formlayout.addRow('Job:', QLineEdit())
        formlayout.addRow('Hobbies:', QLineEdit())
        dlglayout.addLayout(formlayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlglayout.addWidget(btns)
        self.setLayout(dlglayout)


def main():
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
