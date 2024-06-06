import sys
from PyQt5.QtCore import QTextCodec, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QRadioButton,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QSpinBox
)
from PyQt5.QtGui import QIcon
import utils

def show_error(message):
    QMessageBox.critical(main_widget, "Ошибка", message)

def show_info(message):
    QMessageBox.information(main_widget, "Информация", message)

def on_open_click():
    """Реакция на нажатие кнопки "Загрузить из файла"."""
    try:
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Открыть файл",
            "",
            "Текстовые файлы (*.txt *.json *.csv)")

        if file_name == "":
            return

        file_content = utils.open_file(file_name)
        txt_main.setText(file_content)

        show_info("Файл {} открыт.".format(file_name))
    except Exception as err:
        show_error(str(err))

def on_save_click():
    """Реакция на нажатие кнопки "Сохранить в файл..."."""
    try:
        file_name, _ = QFileDialog.getSaveFileName(
            None,
            "Сохранить как...",
            "",
            "Текстовые файлы (*.txt *.json *.csv)")

        if file_name == "":
            return

        text_to_save = txt_main.toPlainText()
        utils.save_file(file_name, text_to_save)

        show_info("Файл {} сохранен.".format(file_name))
    except Exception as err:
        show_error(str(err))

def on_do_crypt_click():
    """Реакция на нажатие кнопки "Выполнить"."""
    try:
        text = txt_main.toPlainText()
        shift = sp_shift.value()

        current_codec = QTextCodec.codecForLocale()

        if rd_encrypt.isChecked():
            result = utils.ceasar(text, shift)
        else:
            result = utils.ceasar(text, -shift)

        txt_main.setText(result)
        QTextCodec.setCodecForLocale(current_codec)
    except Exception as err:
        show_error(str(err))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Главное окно приложения
    main_widget = QWidget()
    main_widget.resize(640, 350)
    main_widget.setWindowTitle("Шифр Цезаря")
    main_widget.setWindowIcon(QIcon('main_icon.png'))

    # 1. Левая часть окна
    vbox_left = QVBoxLayout()

    gb_file_actions = QGroupBox("Текст:")
    vbox_gb_file_actions = QVBoxLayout()

    # 1.1. Открытие/сохранение файлов
    btn_open = QPushButton("Загрузить из файла...")
    btn_save_as = QPushButton("Сохранить в файл...")

    vbox_gb_file_actions.addWidget(btn_open)
    vbox_gb_file_actions.addWidget(btn_save_as)

    gb_file_actions.setLayout(vbox_gb_file_actions)

    # Действия кнопок
    btn_open.clicked.connect(lambda: on_open_click())
    btn_save_as.clicked.connect(lambda: on_save_click())

    # 1.2. Шифрование / дешифрование
    gb_crypt_options = QGroupBox("Режим:")

    rd_encrypt = QRadioButton("Шифрование")
    rd_decrypt = QRadioButton("Дешифрование")
    lbl_shift = QLabel("Сдвиг:")
    sp_shift = QSpinBox()
    sp_shift.setMinimum(1)
    sp_shift.setSingleStep(1)
    btn_do_crypt = QPushButton("Выполнить")
    rd_encrypt.setChecked(True)

    btn_do_crypt.clicked.connect(lambda: on_do_crypt_click())

    vbox_gb_crypt_options = QVBoxLayout()
    vbox_gb_crypt_options.addWidget(rd_encrypt)
    vbox_gb_crypt_options.addWidget(rd_decrypt)
    vbox_gb_crypt_options.addWidget(lbl_shift)
    vbox_gb_crypt_options.addWidget(sp_shift)
    vbox_gb_crypt_options.addWidget(btn_do_crypt)
    gb_crypt_options.setLayout(vbox_gb_crypt_options)

    vbox_left.addWidget(gb_file_actions)
    vbox_left.addWidget(gb_crypt_options)

    # 2. Правая часть окна
    vbox_right = QVBoxLayout()

    lbl_main = QLabel("Текст:")
    txt_main = QTextEdit()

    vbox_right.addWidget(lbl_main)
    vbox_right.addWidget(txt_main)

    # 3. Объединение левой и правой части окна
    hbox = QHBoxLayout()
    hbox.addLayout(vbox_left)
    hbox.addLayout(vbox_right)

    main_widget.setLayout(hbox)

    main_widget.show()
    sys.exit(app.exec_())
