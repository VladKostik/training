import random
import os

path = 'test/data'
os.makedirs(path)

file = open('test/data/text.txt', 'w+')

list_of_tuples = []
for x in range(100):
    my_tuple = (x, random.randint(2,55), random.randint(1,3))
    list_of_tuples.append(my_tuple)
print(list_of_tuples)

list_of_numbers = ''
for tuple in list_of_tuples:
    line = f'{tuple[0]} {tuple[1]} {tuple[2]}'
    file.write(line + '\n')
file.close()

# Good but take a look how it could be solved in more clear way
# import pickle
# import os
#
# from random import randint
#
#
# os.makedirs("test/data")
# operations = []
#
# for _ in range(100):
#     operations.append((randint(1, 100), randint(1, 100), randint(1, 3)))
#
# with open("test/data/text.txt", "wb") as file:
#     pickle.dump(operations, file)
