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
# Good. Proper solution but you make excess movements during solving the task.
# Take a look on lightweight solution from yours.

# some_list = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_list_of_tuples = []
# even_list_of_tuples = []
#
# for index, value in enumerate(some_list):
#     if index % 2 == 0:
#         even_list_of_tuples.append((index, value))
#     else:
#         odd_list_of_tuples.append((index, value))

# or another one alternative solution with updated names and faster
# determining is index is even or odd using bits.
# Odd value always will have 1 in the youngest bit.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# numbers_with_odd_index = []
# numbers_with_event_index = []
#
# for index, value in enumerate(numbers):
#     if bin(index)[-1] == '1':
#         numbers_with_odd_index.append((index, value))
#     else:
#         numbers_with_event_index.append((index, value))
#
# print(numbers_with_event_index)
# print(numbers_with_odd_index)
