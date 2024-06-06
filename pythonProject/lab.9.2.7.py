import numbers

if __name__ == "__main__":
    # Проверка функции gcd
    try:
        a = int(input("Введите первое число для gcd: "))
        b = int(input("Введите второе число для gcd: "))
        gcd_result = numbers.gcd(a, b)
        print(f"gcd({a}, {b}) = {gcd_result}")
    except Exception as e:
        print(f"Ошибка в функции gcd: {e}")

    # Проверка функции lcm
    try:
        a = int(input("Введите первое число для lcm: "))
        b = int(input("Введите второе число для lcm: "))
        lcm_result = numbers.lcm(a, b)
        print(f"lcm({a}, {b}) = {lcm_result}")
    except Exception as e:
        print(f"Ошибка в функции lcm: {e}")

    # Проверка функции is_prime
    try:
        num = int(input("Введите число для проверки на простоту: "))
        is_prime_result = numbers.is_prime(num)
        print(f"is_prime({num}) = {is_prime_result}")
    except Exception as e:
        print(f"Ошибка в функции is_prime: {e}")

    # Проверка функции inverse
    try:
        num = int(input("Введите число для нахождения обратного: "))
        inverse_result = numbers.inverse(num)
        print(f"inverse({num}) = {inverse_result}")
    except Exception as e:
        print(f"Ошибка в функции inverse: {e}")

    # Проверка функции root
    try:
        num = int(input("Введите число для извлечения корня: "))
        root_result = numbers.root(num)
        print(f"root({num}) = {root_result}")
    except Exception as e:
        print(f"Ошибка в функции root: {e}")
