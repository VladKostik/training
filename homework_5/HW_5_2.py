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

