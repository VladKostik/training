# Написать свою реализацию функции filter

from typing import Union, Callable

float_numbers_list = [1.5, 0.6, 3.0, 54.89, 0.57, 10.23, 0.8]
numbers_list = [1, 5, 15, 155, 248, 11, 101, 41, 89, 121]
name_list = [
    'Amalia',
    'Antonio',
    'Benjamin',
    '13',
    '0.5',
    'Adelaide',
    'Dickhead',
    'Baal',
    'George',
    'Victoria'
]
name_tuple = (
    'Amalia',
    'Antonio',
    'Benjamin',
    '13',
    'Adelaide',
    'Dickhead',
    'Albert',
    'George',
    'Victoria'
)
name_dict = {
    'Amalia': 1,
    'Antonio': 2,
    'Benjamin': 3,
    'Adelaide': 4,
    'Dickhead': 5,
    '144': 31,
    'Albert': 6,
    'George': 7,
    'Victoria': 8
}


def my_filter(condition: Callable, sample: Union[list, dict, tuple]) -> list:

    filtered_list = []
    for item in sample:
        if condition(item):
            filtered_list.append(item)
    return filtered_list


def startswith(item):
    """
    Filters iterable objects by first symbol assigned as pattern
    """
    return item.startswith('B')


def is_digit(item):
    """
    Filters iterable objects by symbols recognized as digits
    """
    return item.isdigit()


def floats_compare(item):
    """
    Filters iterable int or float objects using comparing to 1 operators > or <
    """
    return item < 1


def is_odd(item):
    """
    Filters iterable int or float odds
    """
    return item % 2


if __name__ == '__main__':

    print(my_filter(startswith, name_tuple))
    print(my_filter(is_digit, name_dict))
    print(my_filter(floats_compare, float_numbers_list))
    print(my_filter(is_odd, float_numbers_list))
