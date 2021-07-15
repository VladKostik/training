friends = ["John", "Marta", "James", "Amanda", "Marianna"]

print('NAMES'.center(40,'*'))
for friend in friends:
    print(f'{friend.rjust(40)}')

# Good but implemented on ly using methods of string. Use fstrings too.
#  -2 points
