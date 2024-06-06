

import json
import csv


def open_file(file_name):
    """Открытие файла и чтение его содержимого."""
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def save_file(file_name, content):
    """Сохранение содержимого в файл."""
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)


def ceasar(text, shift):
    """Шифрование/дешифрование методом Цезаря."""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result