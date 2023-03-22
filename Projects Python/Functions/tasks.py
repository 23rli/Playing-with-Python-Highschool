#!/usr/bin/python3
# tasks_menu.py
'''Task functions - Execution functions'''
__author__ = "Richard li"
__version__ = "1.0"

import math


def should_answer_cell(is_morn, is_mom, asleep, grumpy):
    """determines if a person should pick up the phone

    :param: is_morn: a boolean for whether its morning or not
    :param: is_mom: a boolean for whether the caller is mom or not
    :param: asleep: a boolean for whether you are asleep or not
    :param: grumpy: a boolean for whether you are grumpy or not
    :return: True if you should pick up the phone, False if not"""

    if asleep:
        return False
    else:
        if is_morn:
            if is_mom:
                return True
            else:
                return False
        else:
            if grumpy:
                return False
    return True


def four_fit_in_one(a, b, c, d, e):
    """determines if one car capacity can fit all the others

    :param: a: a positive integer representing a car's seating capacity
    :param: b: a positive integer representing a car's seating capacity
    :param: c: a positive integer representing a car's seating capacity
    :param: d: a positive integer representing a car's seating capacity
    :param: e: a positive integer representing a car's seating capacity
    :return: True if one car can fit all other capacities, False if not"""

    vars = [a, b, c, d, e]
    sum = 0
    for i in range(5):
        sum += vars[i]

    for i in range(5):
        if sum - vars[i] < vars[i]:
            return vars[i]

    return -1


def get_ticket(speed=70, is_birthday=False):
    """determines how much a person's speeding ticket would be

    :param: speed: a positive integer for driving speed when caught(in mph)
    :param: is_birthday: a boolean for whether or not it's your birthday or not
    :return: positive integer of cost based on speed, or -1 if no ticket"""
    low_ticket = 60
    high_ticket = 80

    if is_birthday:
        low_ticket += 10
        high_ticket += 10

    if speed > high_ticket:
        return speed * 3
    elif speed > low_ticket:
        return speed * 2
    else:
        return 0


def can_move(Nblocked, Sblocked, Eblocked, Wblocked, power, direction):
    """determines if a game character can move in stated direction

    :param: Nblocked: a boolean for whether or not the North is blocked
    :param: Sblocked: a boolean for whether or not the South is blocked
    :param: Eblocked: a boolean for whether or not the East is blocked
    :param: Wblocked: a boolean for whether or not the West is blocked
    :param: power: a positive integer of the power value of said person/icon
    :param: direction: a string stating which direction the person is going in
    :return: True if the person can advance in that direction,
             or False if not"""

    if 14 < power < 100:
        if direction == "N" and not Nblocked:
            return True
        elif direction == "S" and not Sblocked:
            return True
        elif direction == "E" and not Eblocked:
            return True
        elif direction == "W" and not Wblocked:
            return True
    elif power >= 100:
        return True

    return False


def hypotenuse(a, b, c):
    """Determines what the hypotenuse of a right triangle is

    :param: a: a positive integer for one side of the triangle
    :param: b: a positive integer for one side of the triangle
    :param: c: a positive integer for one side of the triangle
    :return: the length or positive integer of the longest side 
             or -1 if not a triangle"""

    if a**2 + b**2 == c**2:
        return c
    elif a**2 + c**2 == b**2:
        return b
    elif c**2 + b**2 == a**2:
        return a
    return -1


def text_pyramid(num_rows, symbol="*", upside_down=False):
    """Determines what the hypotenuse of a right triangle is

    :param: num_rows: a positive integer for one side of the triangle
    :param: symbol: a positive integer for one side of the triangle
    :param: upside_down: a positive integer for one side of the triangle
    :return: the length or positive integer of the longest side 
             or -1 if not a triangle"""
    if symbol == "":
        symbol = "*"
    if upside_down:
        for i in range(num_rows * 2, 0, -2):
            print((num_rows - i // 2) * " " + (i - 1)
                  * symbol + (num_rows - i // 2) * " ")
    else:
        for i in range(0, num_rows * 2, 2):
            print((num_rows - i // 2) * " " + ((i - 1) *
                  symbol) + (num_rows - i // 2) * " ")


def special_primes_counter(start, end, digit):
    """Determines primes through a range ending with a certain digit

    :param: start: a positive integer the beginning of the range(inclusive)
    :param: end: a positive integer the end of the range(inclusive)
    :param: digit: a positive integer from 0-9 for the ones digit
    :return: the an array with the prime numbers"""

    primes = []
    if start <= 1:
        start = 2

    for i in range(start, end + 1):

        if i % 10 == digit:
            prime = False
            range_end = int(math.sqrt(i) + 1)
            for j in range(2, range_end):
                if i % j == 0:
                    prime = True
            if not prime:
                primes.append(i)

    return primes


def draw_painting(char):
    """Determines # of chosen characters, total characters and art

    :param: char: a positive integer the beginning of the range(inclusive)
    :return: the an array with art plus calculations"""

    art1 = [
        "```````_1111111_``````````````````````````````````````",
        "```1$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶$₫_```````````````````````````````",
        "`_111_```````1₫$¶¶¶¶¶¶¶¶¶₫_```````````````````````````",
        "`````````````````_₫¶¶¶¶¶¶¶¶¶₫`````````````````````````",
        "````````````````````1¶¶¶¶¶¶¶¶¶¶₫``````````````````````",
        "```````1₫§₫1``````````₫¶¶¶¶¶¶¶¶¶¶1```_₫1``````````````",
        "```_§$$$¶¶¶¶¶¶¶¶₫_``````§¶¶¶¶¶¶¶¶¶¶1``₫$$1````````````",
        "````````````₫¶¶¶¶¶¶§1````1¶¶¶¶¶¶¶¶¶¶1``1¶¶§_``````````",
        "`````1§§₫1`````₫¶¶¶¶¶¶₫````₫¶¶¶¶$$¶¶¶$``_¶¶$``````````",
        "``````₫¶¶¶¶¶₫```1¶¶¶¶¶¶¶§`````````1¶¶¶$1`1¶¶$1````````",
        "````````_$¶¶¶¶$_`1§¶¶¶¶¶¶¶$1_``````1¶¶¶¶11¶¶¶$````````",
        "``````````1¶¶¶¶§```¶¶¶¶¶¶¶¶¶¶¶1````1¶¶¶¶¶¶¶¶¶¶1```````",
        "```````````§¶¶¶¶§1_1$¶¶¶¶¶¶¶¶¶1```₫¶¶¶¶¶¶¶¶¶¶¶§1``````",
        "````````````1§¶¶¶¶₫``````1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶$1``````",
        "````````````₫¶¶¶¶¶¶1```````1§¶¶¶¶¶¶¶¶¶¶§₫§¶¶¶¶¶₫``````",
        "```````````$¶¶¶¶¶¶¶§``₫¶¶₫11§¶¶¶¶¶¶¶¶¶¶$1_1§¶¶¶§``````",
        "````````````````₫¶¶¶₫`_$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶§111$¶$``````",
        "`````₫§`````````_$¶¶¶11§¶¶¶¶¶¶¶¶¶¶¶¶¶¶$¶¶¶¶§1₫¶¶§`````",
        "`````$¶§````````1¶¶¶§11¶¶¶¶¶¶¶¶¶§₫§¶¶¶$₫$¶¶¶¶¶¶¶¶§````",
        "`````₫¶¶¶§1``_11$¶¶¶11₫¶¶¶¶¶§1_`````1§¶$11¶¶¶¶¶¶¶$1```",
        "``_```₫¶¶¶¶¶¶¶¶¶¶¶$11$¶¶¶¶$1``````````§¶¶§₫§¶¶¶¶¶¶§_``",
        "`₫$1```₫¶¶¶¶¶¶¶¶¶¶$11§¶¶¶¶1````````````1¶$₫₫¶¶¶¶¶¶¶₫``",
        "`₫¶$1```1$¶¶¶¶¶¶¶¶¶§11₫¶¶¶1``````````````1¶¶$$¶¶¶¶$1``",
        "`_$¶¶1````1§¶¶¶¶¶¶¶¶₫_1$¶¶¶1``````````````₫§₫₫$¶¶¶§```",
        "``1¶¶¶1`````₫¶¶¶¶¶¶¶¶$1`1§¶¶¶₫```````````````1¶¶¶¶_```",
        "```₫¶¶¶$````_§¶¶¶¶¶¶¶¶¶₫11111₫11`````````````1¶¶§`````",
        "````₫¶¶¶¶¶₫``1¶¶¶¶¶¶¶¶¶¶¶$§§§$¶¶§`````````````_```````",
        "`````1¶¶¶¶¶11§¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1````````````````````",
        "```````§¶¶¶§₫¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶§````````````````````",
        "```$$```1₫§§$¶¶¶¶1_``1₫$¶¶¶¶¶¶¶¶¶¶1```````````````````",
        "```§¶$1````§¶¶¶₫```````1$¶¶¶¶¶¶¶¶¶₫```````````````````",
        "````§¶¶¶```₫¶¶¶````````1$¶¶¶¶¶¶¶¶¶¶§``````````````````",
        "`````$¶¶¶11$¶¶₫````````1$¶¶¶¶¶¶¶¶¶¶¶§`````````````````",
        "``````₫¶¶¶¶¶¶§1```````1¶¶¶¶¶¶¶$₫1§¶¶¶§````````````````",
        "```````1§¶¶¶$§₫````_$¶¶¶¶¶¶¶¶¶1```1¶¶¶₫```````````````",
        "``````````11₫$₫````_§¶¶¶¶¶¶¶¶¶1```₫¶¶¶¶§``````````````",
        "````````````_§§```````1¶¶¶¶¶¶¶$1``$¶¶¶¶¶₫`````````````",
        "``````````````_````11_``1¶¶¶¶¶¶$``1¶¶¶¶¶§1````````````",
        "````````````````````§¶₫``1$¶¶¶¶¶§``1$¶¶¶¶§````````````",
        "`````````````````````$¶¶1``1¶¶¶¶¶¶```§¶¶¶¶_```````````",
        "`````````````````````1¶¶¶1``1¶¶¶¶¶1```§¶¶¶1```````````",
        "`````````````````````1¶¶¶¶1``1¶¶¶¶¶1``1¶¶¶₫```````````",
        "````````````````````1¶¶¶¶¶$1``₫¶¶¶¶¶_``1¶¶§_``````````",
        "````````````````````1¶¶¶¶¶¶¶1`_$¶¶¶¶1```¶¶§```````````",
        "``````````````````````₫¶¶¶¶¶₫``1$¶¶¶$_``¶¶₫```````````",
        "```````````````````````₫¶¶¶¶$1``₫¶¶¶¶₫``$¶1```````````",
        "````````````````````````₫¶¶¶¶$``1¶¶¶¶§``1§````````````",
        "````````````````````````_$¶¶¶¶1``$¶¶¶$1``_````````````",
        "`````````````````````````₫¶¶¶¶1``§¶¶¶¶1```````````````",
        "`````````````````````````1$¶¶¶1``§¶¶¶$_```````````````",
        "``````````````````````````§¶¶¶₫``₫¶¶¶$````````````````",
        "``````````````````````````§¶¶¶1``§¶¶¶$````````````````",
        "``````````````````````````§¶¶¶1`1¶¶¶¶§````````````````",
        "`````````````````````````1$¶¶¶1`1¶¶¶§1````````````````",
        "`````````````````````````₫¶¶¶₫``§¶¶¶₫`````````````````",
        "````````````````````````1¶¶¶§``1¶¶¶§``````````````````",
        "````````````````````````1¶¶¶1`1¶¶¶§```````````````````",
        "```````````````````````_$¶¶$``₫¶¶¶_```````````````````",
        "``````````````````````1$¶¶§_`₫¶¶§`````````````````````",
        "`````````````````````_$¶¶$``₫¶¶₫``````````````````````",
        "````````````````````1¶¶¶$1`₫¶¶1```````````````````````",
        "```````````````````₫¶¶¶§1`§¶§`````````````````````````",
        "``````````````````§¶¶¶₫``₫§_``````````````````````````",
        "`````````````````§¶¶¶1````````````````````````````````",
        "````````````````₫¶¶$1`````````````````````````````````",
        "```````````````1¶¶¶```````````````````````````````````",
        "``````````````_$¶§_```````````````````````````````````",
        "``````````````₫¶¶`````````````````````````````````````",
        "``````````````§$§`````````````````````````````````````",
        "`````````````1₫₫1`````````````````````````````````````",
    ]

    sumofchar = 0
    total = 0
    print()
    for i in range(len(art1)):
        print(art1[i])
        line = list(art1[i])
        total += len(line)
        for j in range(len(line)):
            if line[j] == char:
                sumofchar += 1

    art1.append("Courtesy of FSymbols\n\n")
    art1.append("# of Character " + char + " = " + str(sumofchar))
    art1.append("Total # of characters = " + str(total))
    return art1
