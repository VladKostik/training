# Создайте функцию которая способна вернуть квадраты четных элементов
# для диапазона  от 0 до 1000000000 включительно.
# Решение должно отрабатывать и не фризить ваш комп.

def crazy_gen():
    """
    Generates square of each even number in range of 0 to 100000000
    """
    number = 0
    while number < 1000000001:
        if number % 2 == 0:
            yield number ** 2
        number += 1


do = crazy_gen()
print(next(do))
print(next(do))
print(next(do))
print(next(do))
print(next(do))
print(next(do))
print(next(do))
print(next(do))
