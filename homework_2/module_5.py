# У вас есть группа людей с неуникальными именами.\
# Сформируйте список не повторяющихся имен (для этой задачи нельзя использовать
# set. Если в списке есть 2 джона нужно взять лишь одного из них.
# "John Dow", "John Dow", "Marta Dow" = > "John Dow", "Marta Dow")

group_of_people = [
    'Alex Sullivan',
    'Johnny Cash',
    'Jack Taller',
    'Elizabeth Smith',
    'Ian O`neel',
    'Jack Taller',
    'Brian Nelson',
    'Robert Vogel',
    'Johnny Cash'
]

# unique_group = set(group_of_people)
# print(unique_group)

# Loop solution

new_list = []
for name in group_of_people:
    if name not in new_list:
        new_list.append(name)

for element in new_list:
    print(element)
# Good. Interesting solution but it could be done with dicts. Since dict keys always unique.
# print(list({}.fromkeys(gruppa).keys()))
#
# Good commit messages but net time try to place them into separate branch

