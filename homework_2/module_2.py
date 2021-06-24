# У вас есть 3 группы людей bingo_blacklist, poker_blacklist, majong_blacklist.
# Имена людей в формате "John Dow" первое и второе имя.
# Найти тех кто состоит во всех черных списках.

bingo_blacklist = {
    'John Snow',
    'Simon Right',
    'Taran Butler',
    'Alice Cooper',
    'Margaret Tetcher'
}
poker_blacklist = {
    'Taran Butler',
    'John Rambo',
    'Alice Cooper',
    'Simon Right',
    'Simon Left',
    'Margaret Tetcher'
}
majong_blacklist = {
    'Margaret Tetcher',
    'Jet Li',
    'John Rambo',
    'Samo Jung',
    'Alice Cooper',
    'Simon Right',
    'Taran Butler'
}

temp_blacklist_1 = bingo_blacklist.intersection(poker_blacklist)
temp_blacklist_2 = majong_blacklist.intersection(temp_blacklist_1)

print('All blacklists gamblers:')
for name in temp_blacklist_2:
    print(name)