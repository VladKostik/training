# Написать свою реализацию функции map
from typing import Callable, Union

float_numbers_list = [1.5, 0.6, 3.0, 54.89, 0.57, 10.23, 0.8]
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

# not bad but I suggest to rename on some another name like callback or func
# 'changes'
def my_map(changes: Callable, some_items: Union[list, tuple, dict]) -> list:

    changed = []
    for item in some_items:
        changed.append(changes(item))
    return changed


def to_str(item):
    """
    Transforms items of iterable object into str
    """

    return str(item)


def add_hello(item):
    """
    Adds 'Hello' to the items of iterable object
    """

    return f'Hello, {item}!'


if __name__ == '__main__':
    print(my_map(to_str, float_numbers_list))
    print(my_map(add_hello, name_dict))

