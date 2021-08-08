#8 Dictionaries

john_name = 'Rambo'  # Good but it is second name only
marta_name = 'Stewart'  # Good but it is second name only
john_age = 33
marta_age = 28
john_salary = 1500.5
marta_salary = 1111.6
john_gender = True
marta_gender = False
john_friends = ['Andrew', 'Simon', 'Jacy']
marta_friends = ['Arthur', 'Sarah', 'Mary']
my_dd_coordinates = (46.4666648, 30.7333304)


john = {
    'Full name:' : f'John {john_name}',
    'Age:' : john_age,
    'Salary:' : john_salary,
    'Gender:' : john_gender,
    'Friends:' : john_friends,
    'Coordinates:' : my_dd_coordinates
}
#print(john)

for key, value in john.items():
    print(key,value)

print()

marta = {
    'Full name:' : f'Marta {marta_name}',
    'Age:' : marta_age,
    'Salary:' : marta_salary,
    'Gender:' : marta_gender,
    'Friends:' : marta_friends,
    'Coordinates:' : my_dd_coordinates
}
#print(marta)

for key, value in marta.items():

    print(key,value)

