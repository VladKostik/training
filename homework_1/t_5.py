# 5 List of friends

john_friends = ['Andrew', 'Simon', 'Jacy']
marta_friends = ['Arthur', 'Sarah', 'Mary']

#Output
common_friends = john_friends + marta_friends

def who_are_friends(common_friends):
    print('Tape name: ')
    name = input()

    if name == 'John':
        i = 0
        while i <= 2:
            print(f'{common_friends[i]} is {name}`s friend')
            i += 1

    elif name == 'Marta':
        i = 3
        while i != 6:
            print(f'{common_friends[i]} is {name}`s friend')
            i += 1
    else:
        print(f'Have no idea who are {name}`s friends')


who_are_friends(common_friends)

who_are_friends(common_friends)


# Good but present some PEP8 small mistakes. Will look on next lesson the common of them. And yes again too much new lines after code
