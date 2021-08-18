# Создать декоратор которые принтит в консоль имя функции которая была вызвана.
# Функция при этом должна работать как и задумывалось.
# К примеру создайте пару функции для арифметических операций
# суммирования и умножения. При вызове этих функций должен возвращаться
# результат операции и предварительно выводиться в консоль имя функции,
# которая была вызвана.


def name_function(any_function):
    def decore(arg1, arg2):
        print(f'Now the {any_function.__name__} will do the magic:')
        return any_function(arg1, arg2)
    return decore


@name_function
def sum_function(x: int, y: int) -> int:
    return x + y


@name_function
def mult_function(w: int, z: int) -> int:
    return w * z


if __name__ == '__main__':
    print(sum_function(2, 5))
    print(mult_function(5, 5))
