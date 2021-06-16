#1 Salary print
john_salary = 1500.5
marta_salary = 1111.6
print(john_salary)
print(marta_salary)

print()

#2 Age print
john_age = 33
marta_age = 28
print(john_age)
print(marta_age)

print()

#3 Name print
john_name = 'Rambo'
marta_name = 'Stewart'
print(john_name)
print(marta_name)

print()

#4 Gender print
john_gender = True
marta_gender = False
print(john_gender)
print(marta_gender)

print()

#5 List of friends
john_friends = ['Andrew', 'Simon', 'Jacy']
marta_friends = ['Arthur', 'Sarah', 'Mary']

print()
#***
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

#who_are_friends(common_friends)

print()

#6 List of people

list_of_people = ['James', 'Caren', 'Ilon', 'James', 'Caren']
print(list_of_people)

print()

set_of_people = set(list_of_people)
print(set_of_people)

print()

#7 Tuples

my_dd_coordinates = (46.4666648, 30.7333304)
print(my_dd_coordinates)

#print(type(my_dd_coordinates))

print()

#8 Dictionaries

john = {'Full name:' : f'John {john_name}', 'Age:' : john_age, 'Salary:' : john_salary,
        'Gender:' : john_gender, 'Friends:' : john_friends, 'Coordinates:' : my_dd_coordinates }
#print(john)

for key, value in john.items():
    print(key,value)

print()

marta = {'Full name:' : f'Marta {marta_name}', 'Age:' : marta_age, 'Salary:' : marta_salary,
        'Gender:' : marta_gender, 'Friends:' : marta_friends, 'Coordinates:' : my_dd_coordinates }
#print(marta)

for key, value in marta.items():
    print(key,value)

print()

#8* Make more people

andrew = {'Full name:': f'Andrew Stivenson', 'Age:': 32, 'Salary:': 1000.02,
          'Gender:': True, 'Friends:': ['Alice', 'John'], 'Coordinates:': my_dd_coordinates}
simon = {'Full name:': f'Simon Smith', 'Age:': 29, 'Salary:': 999.01,
          'Gender:': True, 'Friends:': ['John', 'Ely'], 'Coordinates:': my_dd_coordinates}

john = {'Full name:' : f'John {john_name}', 'Age:' : john_age, 'Salary:' : john_salary,
        'Gender:' : john_gender, 'Friends:' : [andrew, simon], 'Coordinates:' : my_dd_coordinates }

for key, value in john.items():
    print(key,value)

print()

marta_friends = ['Arthur', 'Sarah', 'Mary']
arthur = {'Full name:': f'Arthur Mitchel', 'Age:': 35, 'Salary:': 1805.06,
          'Gender:': True, 'Friends:': ['Marta', 'Mary'], 'Coordinates:': my_dd_coordinates}
sarah = {'Full name:': f'Sarah Connor', 'Age:': 33, 'Salary:': 1200.42,
          'Gender:': False, 'Friends:': ['Abraham', 'T1000'], 'Coordinates:': my_dd_coordinates}

marta = {'Full name:' : f'Marta {marta_name}', 'Age:' : marta_age, 'Salary:' : marta_salary,
        'Gender:' : marta_gender, 'Friends:' : [arthur, sarah], 'Coordinates:' : my_dd_coordinates }

for key, value in marta.items():
    print(key,value)