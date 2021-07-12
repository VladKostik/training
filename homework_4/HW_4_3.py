# 3 есть строка переданная в качестве квери параметров
# "     name=Amanda=sssss&age=32&&salary=1500&currency=" \
#                                                      "quro                             ".
# Преобразовать эту строку в словарь
# где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda......}

text = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "

def parse(sample):

    nospaces = ''.join(sample.split())

    pairs_1 = nospaces.split('&')
    new_list = []
    for pair in pairs_1:
        pair2 = pair.split('=', maxsplit=1)
        # print(pair2)
        new_list.append(pair2)

    i = 0
    new_new_dict = {}
    for pair in new_list:
        if pair == ['']:
            continue
        new_dict = {pair[i]: pair[i + 1]}
        new_new_dict.update(new_dict)
    print(new_new_dict)

parse(text)
