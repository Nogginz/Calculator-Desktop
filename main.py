import design  # Дизайн проекта
import sys  # Нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import os


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это нужно для доступа к переменным, методам
        # и т.п. в дизайне
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        # Мой код:
        self.operation_select = False
        self.first_num = []
        self.second_num = []
        self.stack = []
        self.operand = "none"
        self.press_dot = False

        for n in range(0, 10):
            getattr(self, 'pushButton_%s' % n).pressed.connect(lambda v=n: self.read_num(v))
        self.pushButton_dot.pressed.connect(lambda: self.read_num('.'))
        self.pushButton_delete.pressed.connect(lambda: self.reset())
        self.pushButton_pl.pressed.connect(lambda: self.select_operand('+'))
        self.pushButton_mi.pressed.connect(lambda: self.select_operand('-'))
        self.pushButton_um.pressed.connect(lambda: self.select_operand('*'))
        self.pushButton_del.pressed.connect(lambda: self.select_operand('/'))
        self.pushButton_ravn.pressed.connect(lambda: self.finish())

    def finish(self):
        if len(self.first_num) != 0:
            first_num = float(''.join(self.first_num))
        else:
            first_num = 0.0
        if self.operand != "none":
            second_num = float(''.join(self.second_num))
        if self.operand == '+':
            self.lcdNumber.display(str(first_num + second_num))
        elif self.operand == '-':
            self.lcdNumber.display(str(first_num - second_num))
        elif self.operand == '*':
            self.lcdNumber.display(str(first_num * second_num))
        elif self.operand == '/':
            self.lcdNumber.display(str(first_num / second_num))
        elif self.operand == "none":
            self.lcdNumber.display(str(first_num))

    def select_operand(self, operand):
        self.operand = operand
        self.operation_select = True
        self.press_dot = False

    def reset(self):
        self.operation_select = False
        self.first_num = []
        self.second_num = []
        self.stack = []
        self.lcdNumber.display(0)

    def read_num(self, num):

        if self.operation_select:
            self.second_num.append(str(num))
            self.lcdNumber.display(''.join(self.second_num))
        else:
            self.first_num.append(str(num))
            self.lcdNumber.display(''.join(self.first_num))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()  # показ окна
    app.exec()  # запуск приложения


if __name__ == "__main__":
    main()
