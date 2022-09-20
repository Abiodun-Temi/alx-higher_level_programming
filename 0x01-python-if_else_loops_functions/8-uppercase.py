#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if ord(i) < 97: 
            new_string += i
        else:
            new_variant = ord(i) - 32
            new_string += chr(new_variant)
    print("{:s}".format(new_string), end="")
