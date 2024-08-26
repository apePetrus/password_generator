# simple password generator made in python with random module

import random

char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', 
 '3', '4', '5', '6', '7', '8', '9']

password = []

print('Welcome to password generator\n')

length = int(input('Password characters needed: '))

for i in range(length):
    password.append(random.choice(char_list))

print('Here is your new password:\n')
print(''.join(password))