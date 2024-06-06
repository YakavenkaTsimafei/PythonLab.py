
import word_utils

if __name__ == "__main__":
    # Проверка функции clean
    try:
        clean_result = word_utils.clean("Казнить, нельзя помиловать !?")
        print(f"clean(\"Казнить, нельзя помиловать !?\") = {clean_result}")
    except Exception as e:
        print(f"Ошибка в функции clean: {e}")

    try:
        clean_result = word_utils.clean("")
        print(f"clean(\"\") = {clean_result}")
    except Exception as e:
        print(f"Ошибка в функции clean: {e}")

    # Проверка функции words
    try:
        words_result = word_utils.words("Казнить, нельзя помиловать !?")
        print(f"words(\"Казнить, нельзя помиловать !?\") = {words_result}")
    except Exception as e:
        print(f"Ошибка в функции words: {e}")

    try:
        words_result = word_utils.words("")
        print(f"words(\"\") = {words_result}")
    except Exception as e:
        print(f"Ошибка в функции words: {e}")

    # Проверка функции word_count
    try:
        word_count_result = word_utils.word_count("Казнить, нельзя помиловать !?")
        print(f"word_count(\"Казнить, нельзя помиловать !?\") = {word_count_result}")
    except Exception as e:
        print(f"Ошибка в функции word_count: {e}")

    try:
        word_count_result = word_utils.word_count("")
        print(f"word_count(\"\") = {word_count_result}")
    except Exception as e:
        print(f"Ошибка в функции word_count: {e}")

    # Проверка функции longest_word
    try:
        longest_word_result = word_utils.longest_word("Казнить, нельзя помиловать !?")
        print(f"longest_word(\"Казнить, нельзя помиловать !?\") = {longest_word_result}")
    except Exception as e:
        print(f"Ошибка в функции longest_word: {e}")

    try:
        longest_word_result = word_utils.longest_word("")
        print(f"longest_word(\"\") = {longest_word_result}")
    except Exception as e:
        print(f"Ошибка в функции longest_word: {e}")

    # Проверка функции char_stats
    try:
        char_stats_result = word_utils.char_stats("Daddy!?")
        print(f"char_stats(\"Daddy?\") = {char_stats_result}")
    except Exception as e:
        print(f"Ошибка в функции char_stats: {e}")

    try:
        char_stats_result = word_utils.char_stats("")
        print(f"char_stats(\"\") = {char_stats_result}")
    except Exception as e:
        print(f"Ошибка в функции char_stats: {e}")