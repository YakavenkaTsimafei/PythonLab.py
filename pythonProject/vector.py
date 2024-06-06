

import math


def create(x1, y1, x2, y2):
    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
        raise TypeError("Аргументы должны быть числами типа int или float")

    return {"start": [x1, y1], "end": [x2, y2]}


def is_vector(vector):
    return isinstance(vector, dict) and "start" in vector and "end" in vector


def length(vector):
    if not is_vector(vector):
        raise TypeError("Аргумент должен быть вектором")

    start = vector["start"]
    end = vector["end"]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def multiply(vector, num):
    if not is_vector(vector):
        raise TypeError("Аргумент должен быть вектором")

    multiplied_vector = dict(vector)
    multiplied_vector["end"][0] *= num
    multiplied_vector["end"][1] *= num
    return multiplied_vector


def scalar_product(vector1, vector2):
    if not (is_vector(vector1) and is_vector(vector2)):
        raise TypeError("Аргументы должны быть векторами")

    start1 = vector1["start"]
    end1 = vector1["end"]
    start2 = vector2["start"]
    end2 = vector2["end"]
    dx1 = end1[0] - start1[0]
    dy1 = end1[1] - start1[1]
    dx2 = end2[0] - start2[0]
    dy2 = end2[1] - start2[1]
    return dx1 * dx2 + dy1 * dy2


def angle_between(vector1, vector2):
    if not (is_vector(vector1) and is_vector(vector2)):
        raise TypeError("Аргументы должны быть векторами")

    dot_product = scalar_product(vector1, vector2)
    length1 = length(vector1)
    length2 = length(vector2)
    cosine = dot_product / (length1 * length2)
    radians = math.acos(cosine)
    degrees = math.degrees(radians)
    return degrees