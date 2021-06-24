#У вас есть 2 компании с людьми.
# Одна из компаний пусть будет это global_logic была поглощена компанией toshiba.
# Отобразите это в коде. Учитывайте что люди с одинаковыми именами могут быть в обеих компаниях

global_logic = [
    'John Connor',
    'Sarah Connor',
    'James Smith',
    'Elvis Presley',
    'Soichiro Honda'
]

toshiba = [
    'Arai Tsunehiro',
    'Musasi Miyamoto',
    'Kiyoshi Yamazaki',
    'James Smith'
]

toshiba.extend(global_logic)
<<<<<<< HEAD
print(toshiba)

print()

# Better view
print('Toshiba Company employees:')
i = 1
for element in toshiba:
    print(f'{i}. {element}')
    i += 1
=======
print(toshiba)
>>>>>>> homework_1
