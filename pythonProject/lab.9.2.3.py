import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QGridLayout,
    QHBoxLayout,
    QPushButton,
    QGroupBox,
    QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# Масштабирование для 4K-Мониторов
import PyQt5
QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling, True)


def make_operation(a, b, op):
    """Вернуть результат операции 'op' над 'a' и 'b'.

    Параметры:
        - a (int): первое число;
        - b (int): первое число;
        - op (str): операция над числами ("+", "-", "*", "/", "//", "%").

    Результат:
        - int, float или None (если нет такой операции).
    """
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "//":
        return a // b
    elif op == "%":
        return a % b
    else:
        return None


def on_click(op):
    try:
        x = int(edt_x.text())
        y = int(edt_y.text())
        edt_res.setText("{}".format(make_operation(x, y, op)))
    except Exception as err:
        # Текст ошибки выводится в текстовое поле и терминал
        print(type(err), err)
        edt_res.setText("Не могу выполнить операцию!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Главное окно приложения
    w = QWidget()
    w.setFixedSize(400, 150)
    w.setWindowTitle("Мини-калькулятор")
    w.setWindowIcon(QIcon('main_icon.png'))

    # Общее расположение элементов - сетка
    grid = QGridLayout()
    grid.setSpacing(10)

    # 1-е метка
    lbl_x = QLabel("Первое число:")
    # 2-е метка
    lbl_y = QLabel("Второе число:")
    # Метка для результата
    lbl_res = QLabel("Результат:")

    buttons_layout = QHBoxLayout()
    grid.setSpacing(5)

    # Кнопки
    btn_add = QPushButton("+")
    btn_add.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    btn_sub = QPushButton("-")
    btn_sub.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    btn_mul = QPushButton("*")
    btn_mul.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    btn_div = QPushButton("/")
    btn_div.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    btn_floor_div = QPushButton("//")
    btn_floor_div.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    btn_mod = QPushButton("%")
    btn_mod.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    buttons_layout.addWidget(btn_add)
    buttons_layout.addWidget(btn_sub)
    buttons_layout.addWidget(btn_mul)
    buttons_layout.addWidget(btn_div)
    buttons_layout.addWidget(btn_floor_div)
    buttons_layout.addWidget(btn_mod)

    # Действия кнопок
    btn_add.clicked.connect(lambda: on_click("+"))
    btn_sub.clicked.connect(lambda: on_click("-"))
    btn_mul.clicked.connect(lambda: on_click("*"))
    btn_div.clicked.connect(lambda: on_click("/"))
    btn_floor_div.clicked.connect(lambda: on_click("//"))
    btn_mod.clicked.connect(lambda: on_click("%"))

    # 1-е текстовое поле
    edt_x = QLineEdit()
    edt_x.setAlignment(Qt.AlignCenter)
    # 2-е текстовое поле
    edt_y = QLineEdit()
    edt_y.setAlignment(Qt.AlignCenter)
    # Поле для результата
    edt_res = QLineEdit()
    edt_res.setAlignment(Qt.AlignCenter)
    edt_res.setReadOnly(True)

    gb_ops = QGroupBox("Операции")
    gb_ops.setLayout(buttons_layout)

    # Общее расположение элементов
    grid.addWidget(lbl_x, 0, 0, Qt.AlignRight)
    grid.addWidget(edt_x, 0, 1)
    grid.addWidget(lbl_y, 0, 2, Qt.AlignRight)
    grid.addWidget(edt_y, 0, 3)
    grid.addWidget(gb_ops, 1, 0, 1, 4)
    grid.addWidget(lbl_res, 2, 0, Qt.AlignRight)
    grid.addWidget(edt_res, 2, 1, 1, 3)

    # Запуск приложения
    w.setLayout(grid)
    w.show()
    sys.exit(app.exec_())