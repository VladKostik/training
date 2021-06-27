#8* Make more people

john_name = 'Rambo'
marta_name = 'Stewart'
john_age = 33
marta_age = 28
john_salary = 1500.5
marta_salary = 1111.6
john_gender = True
marta_gender = False
my_dd_coordinates = (46.4666648, 30.7333304)

andrew = {
    'Full name:': f'Andrew Stivenson',
    'Age:': 32,
    'Salary:': 1000.02,
    'Gender:': True,
    'Friends:': ['Alice', 'John'],
    'Coordinates:': my_dd_coordinates
}
simon = {
    'Full name:': f'Simon Smith',
    'Age:': 29,
    'Salary:': 999.01,
    'Gender:': True,
    'Friends:': ['John', 'Ely'],
    'Coordinates:': my_dd_coordinates
}


#John
john = {
    'Full name:' : f'John {john_name}',
    'Age:' : john_age,
    'Salary:' : john_salary,
    'Gender:' : john_gender,
    'Friends:' : [andrew, simon],
    'Coordinates:' : my_dd_coordinates
}

for key, value in john.items():
    print(key,value)

print()

#Marta
marta_friends = ['Arthur', 'Sarah', 'Mary']
arthur = {
    'Full name:': f'Arthur Mitchel',
    'Age:': 35, 'Salary:': 1805.06,
    'Gender:': True,
    'Friends:': ['Marta', 'Mary'],
    'Coordinates:': my_dd_coordinates
}
sarah = {
    'Full name:': f'Sarah Connor',
    'Age:': 33,
    'Salary:': 1200.42,
    'Gender:': False,
    'Friends:': ['Abraham', 'T1000'],
    'Coordinates:': my_dd_coordinates
}

marta = {
    'Full name:' : f'Marta {marta_name}',
    'Age:' : marta_age,
    'Salary:' : marta_salary,
    'Gender:' : marta_gender,
    'Friends:' : [arthur, sarah],
    'Coordinates:' : my_dd_coordinates
}

for key, value in marta.items():
    print(key,value)

# Good but it could be described and printed in console in more elegant way:
# john = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 25,
#     "gender": "male",
#     "parents": ["John Smith Junio", "Marta Smith"]
# }
#  Look on how dict is described. It is more preferable view on real projects.
# print(john)
#
#
# for key, value in john.items():
#     # print(key, value, sep=" => ")
#     print(f"{key} => {value}")
# Also you may notice that there is no way to define some friends which are not defined yet. It was some trap in requirements. So next time clarify requiements.
