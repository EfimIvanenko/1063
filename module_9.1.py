def apply_all_func(int_list, *functions):
    """
    Применяет все переданные функции к списку чисел и возвращает результаты.

    :param int_list: Список чисел (int или float).
    :param functions: Набор функций для применения к списку.
    :return: Словарь с именами функций и их результатами.
    """
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
