# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
# ● Формула корреляции Пирсона: https://www.codecamp.ru/blog/pearson-correlation-coefficient/
# Встроенные функции не использовать!!!
def get_len_list(my_list: list) -> int:
    """Функция вычисления длины списка"""
    count = 0
    for _ in my_list:
        count += 1
    return count


def get_sum_list(my_list: list) -> int:
    """Функция вычисления сумы элементов списка"""
    sum_list = 0
    for item in my_list:
        sum_list += item
    return sum_list


def get_avg_list(my_list: list) -> float:
    """Функция вычисления среднего значения элементов списка"""
    return get_sum_list(my_list) / get_len_list(my_list)


def get_sum_two_list_sub(list_x: list, list_y: list) -> int:
    """Функция вычисления числителя в формуле для нахождения коэффициента корреляции Пирсона"""
    if get_len_list(list_x) == get_len_list(list_y):
        mean_x = get_avg_list(list_x)
        mean_y = get_avg_list(list_y)
        return get_sum_list([(list_x[i] - mean_x) * (list_y[i] - mean_y) for i in range(len(list_x))])
    return 0


def get_sum_list_sub_squared(my_list: list) -> float:
    """Функция вычисления суммы среднеквадратичного отклонения элементов списка"""
    mean_list = get_avg_list(my_list)
    return get_sum_list([(item - mean_list) ** 2 for item in my_list])


def get_pearson_correlation(list_x: list, list_y: list) -> float:
    """Функция вычисления коэффициента корреляции Пирсона"""
    # print(f'Числитель: {get_sum_two_list_sub(list_x, list_y)}')
    # print(f'Знаменатель: {((get_sum_list_sub_squared(list_x) * get_sum_list_sub_squared(list_y)) ** 0.5)}')
    return get_sum_two_list_sub(list_x, list_y) / ((get_sum_list_sub_squared(list_x) * get_sum_list_sub_squared(list_y)) ** 0.5)


if __name__ == '__main__':
    # данные для теста с сайта https://www.codecamp.ru/blog/pearson-correlation-coefficient/
    list_x = [2, 4, 6, 8]
    list_y = [2, 4, 10, 12]
    print(get_pearson_correlation(list_x, list_y))