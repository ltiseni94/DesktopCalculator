import functools

class Controller(object):
    __error = False

    def __init__(self, view, error_message = 'ERROR'):
        self.__view = view
        self.__error_message = error_message
        self.__connectEvents()

    def __buildExpression(self, btnText):
        if self.__error:
            self.__clearDisplay()
            self.__error = False

        expression = self.__view.getDisplayText() + btnText
        self.__view.setDisplayText(expression)

    def __calculateResult(self):
        expression = self.__view.getDisplayText()
        result = self.__evaluateExpression(expression)
        self.__view.setDisplayText(result)

    def __clearDisplay(self):
        self.__view.setDisplayText('')

    def __connectEvents(self):
        for btnText, btn in self.__view.buttons.items():
            if btnText not in ['=', 'C']:
                btn.clicked.connect(functools.partial(self.__buildExpression, btnText))

        self.__view.buttons['='].clicked.connect(self.__calculateResult)
        self.__view.buttons['C'].clicked.connect(self.__clearDisplay)
        self.__view.display.returnPressed.connect(self.__calculateResult)

    def __evaluateExpression(self, expression):
        try:
            return str(eval(expression, {}, {}))
        except:
            self.__error = True
            return self.__error_message
