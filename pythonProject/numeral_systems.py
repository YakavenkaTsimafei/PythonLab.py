

LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


class WrongBaseError(ValueError):
    pass


def tenth_to_base(number, base):
    """Преобразовать десятичное число 'number' в систему счисления 'base'.

    Параметры:
        number (int): Десятичное число.
        base (int): Целевая система счисления (2-16).

    Возвращает:
        str: Число в системе счисления 'base'.

    Исключения:
        WrongBaseError: Если 'base' не находится в допустимом диапазоне (2-16).
    """
    if base < 2 or base > 16:
        raise WrongBaseError("Недопустимая система счисления")
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            result = LETTERS_EX[remainder] + result
        else:
            result = str(remainder) + result
        number = number // base
    return result


def base_to_tenth(number, base):
    """Преобразовать число 'number' в десятичную систему счисления из системы счисления 'base'.

    Параметры:
        number (str): Число в системе счисления 'base'.
        base (int): Основание системы счисления (2-16).

    Возвращает:
        int: Число в десятичной системе счисления.

    Исключения:
        WrongBaseError: Если число 'number' не существует в системе счисления 'base' или
                        если 'base' не находится в допустимом диапазоне (2-16).
    """
    if base < 2 or base > 16:
        raise WrongBaseError("Недопустимая система счисления")
    result = 0
    power = len(number) - 1
    for digit in number:
        if digit.isdigit():
            value = int(digit)
        else:
            value = DIGITS_EX.get(digit.upper())
            if value is None:
                raise WrongBaseError(f"Недопустимая цифра '{digit}' в системе счисления")
        if value >= base:
            raise WrongBaseError(f"Цифра '{digit}' не существует в системе счисления с основанием '{base}'")
        result += value * (base ** power)
        power -= 1
    return result




def convert(number, from_base, to_base):
    """Преобразовать число из одной системы счисления в другую.

    Параметры:
        number (str или int): Число для преобразования.
        from_base (int): Основание текущей системы счисления.
        to_base (int): Основание целевой системы счисления.

    Возвращает:
        str: Преобразованное число в целевой системе счисления.

    Исключения:
        WrongBaseError: Если 'from_base' или 'to_base' не находятся в допустимом диапазоне (2-16).
    """
    if isinstance(number, int):
        decimal_number = number
    elif isinstance(number, str):
        decimal_number = base_to_tenth(number, from_base)
    else:
        raise ValueError("Недопустимый формат числа")
    return tenth_to_base(decimal_number, to_base)