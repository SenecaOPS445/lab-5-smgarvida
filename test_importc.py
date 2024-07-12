#!/usr/bin/env python3
# Author ID: smgarvida

import lab5c

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        result = int(number1) + int(number2)
        return result
    except TypeError:
        return 'error: could not add numbers'
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except FileNotFoundError:
        return 'error: could not read file'
    except IOError:
        return 'error: could not read file'

if __name__ == '__main__':

    print(lab5c.add(10, 5))                 # 15
    print(lab5c.add('10', 5))               # 15
    print(lab5c.add('10', '5'))             # 15
    print(lab5c.add('abc', '5'))            # 'error: could not add numbers'
    print(lab5c.add('hello', 'world'))      # 'error: could not add numbers'

    print(lab5c.read_file('seneca2.txt'))   # ['Line 1\n', 'Line 2\n', 'Line 3\n']
    print(lab5c.read_file('file10000.txt')) # 'error: could not read file'

