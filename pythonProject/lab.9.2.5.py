
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QGridLayout,
    QPushButton,
    QSizePolicy,
    QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import numeral_systems


def on_click():
    """Реакция на нажатие кнопки."""
    try:
        number = int(edt_num.text())  # Получить число из текстового поля
        base1 = int(cbb_from_base.currentText())
        base2 = int(cbb_to_base.currentText())  # Получить основание целевой с.с. для перевода
        res = numeral_systems.convert(number, base1, base2)  # Вызвать numeral_systems.convert(...)
        edt_res.setText(str(res))  # Вывести результат в текстовое поле
    except Exception as err:
        print(err)  # Вывести текст ошибки в терминал
        edt_res.setText("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Главное окно приложения
    w = QWidget()
    w.resize(365, 230)
    w.setWindowTitle("Системы счисления - переводы")
    w.setWindowIcon(QIcon('main_icon.png'))

    # Общее расположение элементов - сетка
    grid = QGridLayout()
    grid.setSpacing(15)

    # Метки
    lbl_num = QLabel("Число:")
    lbl_from_base = QLabel("Из (с.с.):")
    lbl_to_base = QLabel("В (с.с.):")
    lbl_res = QLabel("Итог:")

    # Кнопки
    btn_convert = QPushButton("Преобразовать")
    btn_convert.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Действия кнопок
    btn_convert.clicked.connect(lambda: on_click())

    # Текстовые поля
    edt_num = QLineEdit()
    edt_num.setAlignment(Qt.AlignCenter)
    edt_res = QLineEdit()
    edt_res.setAlignment(Qt.AlignCenter)
    edt_res.setReadOnly(True)

    # Выпадающие списки с.с.
    cbb_from_base = QComboBox()
    cbb_to_base = QComboBox()
    for i in range(2, 17):
        cbb_from_base.addItem(str(i))
        cbb_to_base.addItem(str(i))
    cbb_from_base.setCurrentText("10")

    # Общее расположение элементов
    grid.addWidget(lbl_num, 0, 0, Qt.AlignRight)
    grid.addWidget(edt_num, 0, 1, 1, 3)
    grid.addWidget(lbl_from_base, 1, 0, Qt.AlignRight)
    grid.addWidget(cbb_from_base, 1, 1)
    grid.addWidget(lbl_to_base, 1, 2, Qt.AlignRight)
    grid.addWidget(cbb_to_base, 1, 3)
    grid.addWidget(btn_convert, 2, 1, 1, 3)
    grid.addWidget(lbl_res, 3, 0, Qt.AlignRight)
    grid.addWidget(edt_res, 3, 1, 1, 3)

    # Запуск приложения
    w.setLayout(grid)
    w.show()
    sys.exit(app.exec_())
