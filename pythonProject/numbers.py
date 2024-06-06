
def gcd(first, second):
    if not isinstance(first, int) or not isinstance(second, int):
        raise TypeError("Аргументы должны быть целыми числами")
    if first == 0 or second == 0:
        raise ValueError("Аргументы не могут быть равны 0")

    while second != 0:
        first, second = second, first % second

    return abs(first)


def lcm(first, second):
    if not isinstance(first, int) or not isinstance(second, int):
        raise TypeError("Аргументы должны быть целыми числами")
    if first == 0 or second == 0:
        raise ValueError("Аргументы не могут быть равны 0")

    return abs(first * second) // gcd(first, second)


def is_prime(number):
    if not isinstance(number, int):
        raise TypeError("Аргумент должен быть целым числом")
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def inverse(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    if number == 0:
        raise ZeroDivisionError("Аргумент не может быть равен 0")

    return 1 / number


def root(number, power=2):
    if not isinstance(number, (int, float)) or not isinstance(power, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    if power < 1:
        raise ValueError("Степень должна быть больше или равна 1")

    return number ** (1 / power)