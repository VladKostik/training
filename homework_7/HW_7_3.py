# Написать свою реализацию функции reduce
from functools import reduce
from typing import Callable, Union
from operator import add, mul


numbers_list = [1, 5, 15, -155, 248, -11, 101, 41, -89, 121]


def my_reduce(
        operation: Callable,
        items: Union[list, dict, tuple],
        start: Union[str, int, float]
) -> Union[str, int, float]:

    aggregate = start
    for item in items:
        aggregate = operation(aggregate, item)
    return aggregate


if __name__ == '__main__':
    print(my_reduce(add, numbers_list, 0))
    print(my_reduce(mul, numbers_list, 1))
    print(my_reduce(lambda a, b: a if a > b else b, numbers_list))
    # start argument is excessive

    # take a look on dignature of reduce function
    # reduce()
 # -1 point

