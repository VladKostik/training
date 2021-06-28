# У вас есть 2 списка имен friends = ["John", "Marta", "James"] и
# enamies = ["John", "Johnatan", "Artur"].
# Перебрать имена друзей и написать сообщение
# f"{friend} we are the best friends"
# если друг не оказался в списке имен врагов.
# И вывести сообщение f"{friend} we are not the friends anymore"
# если друг оказался в списке врагов.
# Если имя друга James не проверяем его ибо он лучшый друг.

# friends = ["John", "Marta", "James", 'Johnatan']
# enemies = ["John", "Johnatan", "Artur"]
#
# it = iter(friends)
# for friend in friends:
#     if friend == 'James':
#         next(it)  # This command does not do anything here so it is excess
#     elif friend not in enemies:
#         print(f'{friend} we are the best friends')
#     else:
#         print(f'{friend} we are not friends anymore')

# Good solution but lets try to improove it in some way:
# Solution 1:
# friends = ["John", "Marta", "James", 'Johnatan']
# enemies = ["John", "Johnatan", "Artur"]
#
# for friend in friends:
#     if friend == 'James':
#         pass
#     elif friend not in enemies:
#         print(f'{friend} we are the best friends')
#     else:
#         print(f'{friend} we are not friends anymore')

# Solution 2:
# friends = ["John", "Marta", "James", 'Johnatan']
# enemies = ["John", "Johnatan", "Artur"]
#
# for friend in friends:
#     if friend not in enemies and friend != 'James':
#         print(f'{friend} we are the best friends')
#     elif friend in enemies:
#         print(f'{friend} we are not friends anymore')
