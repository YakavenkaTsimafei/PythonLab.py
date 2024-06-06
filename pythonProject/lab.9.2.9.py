

import vector

if __name__ == "__main__":
    # Проверка функции create
    try:
        vector1 = vector.create(1, 2, 3, 4)
        print(f"create(1, 2, 3, 4) = {vector1}")
    except Exception as e:
        print(f"Ошибка в функции create: {e}")

    # Проверка функции is_vector
    try:
        is_vector_result = vector.is_vector(vector1)
        print(f"is_vector(vector1) = {is_vector_result}")
    except Exception as e:
        print(f"Ошибка в функции is_vector: {e}")

    # Проверка функции length
    try:
        length_result = vector.length(vector1)
        print(f"length(vector1) = {length_result}")
    except Exception as e:
        print(f"Ошибка в функции length: {e}")

    # Проверка функции multiply
    try:
        multiplied_vector = vector.multiply(vector1, 2)
        print(f"multiply(vector1, 2) = {multiplied_vector}")
    except Exception as e:
        print(f"Ошибка в функции multiply: {e}")

    # Проверка функции scalar_product
    try:
        vector2 = vector.create(5, 6, 7, 8)
        scalar_product_result = vector.scalar_product(vector1, vector2)
        print(f"scalar_product(vector1, vector2) = {scalar_product_result}")
    except Exception as e:
        print(f"Ошибка в функции scalar_product: {e}")

    # Проверка функции angle_between
    try:
        angle_result = vector.angle_between(vector1, vector2)
        print(f"angle_between(vector1, vector2) = {angle_result} degrees")
    except Exception as e:
        print(f"Ошибка в функции angle_between: {e}")