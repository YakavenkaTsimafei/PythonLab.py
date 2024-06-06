import roman

# Ввод римского и арабского числа
roman_number = input("Введите римское число: ")
arabic_number = int(input("Введите арабское число: "))

# Преобразование римского числа в арабское
arabic_from_roman = roman.fromRoman(roman_number)

# Арифметические операции
addition = arabic_from_roman + arabic_number
subtraction = arabic_from_roman - arabic_number
multiplication = arabic_from_roman * arabic_number
floor_division = arabic_from_roman // arabic_number

# Преобразование результатов в римские числа
addition_roman = roman.toRoman(addition)
subtraction_roman = roman.toRoman(subtraction)
multiplication_roman = roman.toRoman(multiplication)
floor_division_roman = roman.toRoman(floor_division)

# Вывод результатов
print(f"{arabic_from_roman} + {arabic_number} = {addition} (римское: {addition_roman})")
print(f"{arabic_from_roman} - {arabic_number} = {subtraction} (римское: {subtraction_roman})")
print(f"{arabic_from_roman} * {arabic_number} = {multiplication} (римское: {multiplication_roman})")
print(f"{arabic_from_roman} // {arabic_number} = {floor_division} (римское: {floor_division_roman})")
