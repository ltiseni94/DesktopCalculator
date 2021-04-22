from PyQt5.QtWidgets import QPushButton

class Buttons(object):

    texts = [
        '7', '8', '9', '/', 'C',
        '4', '5', '6', '*', '(',
        '1', '2', '3', '-', ')',
        '0', '00', '.', '+', '='
    ]

    __buttons = {}

    def __init__(self, layout, btnSize = (40, 40), columns = 5):
        for index in range(len(self.texts)):
            text = self.texts[index]
            position = divmod(index, columns)

            button = QPushButton(text)
            button.setFixedSize(*btnSize)
            layout.addWidget(button, *position)

            self.__buttons[text] = button

    def __getitem__(self, key):
        return self.__buttons[key]

    def items(self):
        return self.__buttons.items()
