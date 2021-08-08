# у вас есть список элементов [1, 2, 3, 4, 5, 6, 7, 8].
# Перебрать список используя foreach цыкл .
# Элемент с нечетным индексом поместить в новый список кортежей,
# где первый элемент это индекс а второй это значение. [(index, value)].
# соответственно элементы с четным индексом поместить в другой список
# кортежей с тем же форматом что и в случае с нечетными индексами.

values = [1, 2, 3, 4, 5, 6, 7, 8]

odd_list = []
even_list = []
for value in values:
    if values.index(value) % 2 != 0:
        temp = (values.index(value), value)
        odd_list += temp,
    else:
        temp = (values.index(value), value)
        even_list += temp,
print(odd_list)
print(even_list)