from homework_9.dir.dir1 import add, divide, mult


def some_function(a: int, b: int) -> list:

    my_list = []
    result1 = add(a, b)
    my_list.append(result1)
    result2 = mult(a, b)
    my_list.append(result2)
    result3 = divide(result2, result1)
    my_list.append(result3)

    return my_list


print(some_function(6, 4))
