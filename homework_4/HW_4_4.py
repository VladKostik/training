# 4 у вас есть список имен переменных в формате
# кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать
# его в список имен переменных для пайтона в формате
# снейк кейс ["first_item", "friends_list", "my_tuple"]


import re

list_of_names = ["FirstItem", "FriendsList", "MyTuple"]

new_list_of_names = []
for name in list_of_names:
    new_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    new_list_of_names.append(new_name)
print(new_list_of_names)

