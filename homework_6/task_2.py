from typing import Tuple, Union


def square(side: float) -> tuple:
    """
    Returns square perimeter, area and diagonal
    """
    perimeter = side*4
    area = side**2
    diagonal = side**0.5
    return round(perimeter, 2), round(area, 2), round(diagonal, 2)


if __name__ == "__main__":
    print(square(1.8))

# Good. But take a look on warnings which provide Pycahrm for you
# return type hint also could be modified:
# Tuple[Union[int, float], Union[int, float], Union[int, float]]

