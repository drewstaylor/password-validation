#!/usr/bin/python3

import sys

def password_check(passwd):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    isValid = False

    if len(passwd) < 15:
        print('Password should be at least 15 characters, got: ' + str(len(passwd)))
    if not any(char.isdigit() for char in passwd):
        print('Password should contain at least one number')
    if not any(char.isupper() for char in passwd):
        print('Password should contain at least one uppercase character')
    if not any(char.islower() for char in passwd):
        print('Password should contain at least one lowercase character')
    if not any(char in symbols for char in passwd):
        print('Password should contain at least one special character from list: ', symbols)

    if len(passwd) >= 15 and any(char.isdigit() for char in passwd) and any(char.isupper() for char in passwd) and any(char.islower() for char in passwd) and any(char in symbols for char in passwd):
        isValid = True

    return isValid

arguments = sys.argv
if len(arguments) < 2:
    print('No password could be parsed by argv')
    valid_password = False
else:
    password = arguments[1]
    print('Testing password: ', password)
    valid_password = password_check(password)

print('Password is valid: ', valid_password)
