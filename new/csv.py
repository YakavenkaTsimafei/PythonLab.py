import random
import csv
from transliterate import translit
import time

txt_file_path = "1.txt"
with open(txt_file_path, "r", encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

faculty = input("Введите факультет: ")
admission_year = input("Введите год поступления: ")
group = input("Введите группу: ")

csv_data = []
start_time = time.time()

username_english = translit(f"{group}{admission_year}", 'ru', reversed=True)

for line in lines:
    full_name = line.strip()
    last_name, first_name, middle_name = full_name.split(maxsplit=2)
    username = f"{first_name[0]}{last_name}{admission_year}"
    password = random.randint(1000, 9999)
    email = f"{username_english}.{faculty}@Gmail.com"
    csv_data.append([last_name, first_name, middle_name, password, email, "Гомель", 0, faculty, group + admission_year, 3])

csv_file_path = "students.csv"
with open(csv_file_path, "w", newline="", encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["Фамилия", "Имя", "Отчество", "Пароль", "Email", "Город", "maildisplay", "Факультет", "Группа", "Курс"])
    writer.writerows(csv_data)

print(f"CSV файл успешно создан: {csv_file_path}")

end_time = time.time()
print(f"Время работы программы: {end_time - start_time} ")
