

import string


def clean(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    return cleaned_text


def words(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    cleaned_text = clean(text)
    word_list = cleaned_text.split()
    return tuple(word_list)


def word_count(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    word_list = words(text)
    return len(word_list)


def longest_word(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    word_list = words(text)
    if not word_list:
        return ""

    longest = max(word_list, key=len)
    return longest


def char_stats(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    cleaned_text = clean(text)
    stats = {}

    for char in cleaned_text:
        stats[char] = stats.get(char, 0) + 1

    return stats