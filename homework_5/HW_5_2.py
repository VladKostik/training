with open('test/data/text.txt') as file:
    lines = file.readlines()

    for line in lines:
        new_line = line.split(' ')

        if int(new_line[2].strip()) == 1:
            print(int(new_line[0]) + int(new_line[1]))
        elif int(new_line[2].strip()) == 2:
            print(int(new_line[0]) - int(new_line[1]))
        else:
            print(int(new_line[0]) * int(new_line[1]))

# Good but take a look how it could be done with pickle
# import pickle
#
# with open('test/data/text.txt', "rb") as file:
#     operations = pickle.load(file)
#
#     for operation in operations:
#         left, right, operator = operation
#         if operator == 1:
#             print(f"{left} + {right} = {left + right}")
#         elif operator == 2:
#             print(f"{left} * {right} = {left * right}")
#         else:
#             print(f"{left} / {right} = {left / right}")
