# Домашнее задание 1

from random import randint


# генератор списка случайных чисел
def get_list(len_list: int) -> list:
    return [randint(0, 10) for _ in range(0, len_list)]


# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def sort_list_imperative(numbers: list) -> list:
    # длина списка в императивном стиле
    len_list = 0
    for _ in numbers:
        len_list += 1
    # пузырьковая сортировка
    were_replacements = True
    while were_replacements:
        were_replacements = False
        for i in range(0, len_list - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i+1], numbers[i]
                were_replacements = True
    return numbers


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative_1(numbers: list) -> list:
    numbers.sort(reverse=True)
    return numbers


def sort_list_declarative_2(numbers: list) -> list:
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    random_list = get_list(20)
    print(f'Исходный список {random_list}')
    print(sort_list_imperative(random_list[:]))
    print(sort_list_declarative_1(random_list[:]))
    print(sort_list_declarative_2(random_list[:]))