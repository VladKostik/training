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
print(toshiba)

# better view
print('Toshiba Comp. employees:')
i = 1
for name in toshiba:
    print(f'{i}. {name}')
    i += 1

