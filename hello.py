import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


def main():
    app = QApplication(sys.argv)    # if args should be passed
    # app = QApplication([])        # if no args are needed
    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(100, 100, 280, 80)
    window.move(60, 15)
    helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
    helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
