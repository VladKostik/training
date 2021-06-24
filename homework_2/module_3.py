# У вас есть две группы людей.
# В одной группе состоят всеядные люди в другой лишь вегетарианцы.
# Всеядный является вегетарианцем но вегетарианец не является всеядным.
# Вывести список гостей которые могут есть овощи и зелень.

all_eaters = ['Jeck Lincoln', 'Robert Smith', 'Jerry Miculek', 'Antony Hopkins']
vegetarians = ['Adolf Schiklgruber', 'Mahatma Gandhi', 'Oleg Popov']

vegetarians.extend(all_eaters)
print('Guests who can eat vegetables:')
i = 1
for name in vegetarians:
    print(f'{i}. {name}')
    i += 1

