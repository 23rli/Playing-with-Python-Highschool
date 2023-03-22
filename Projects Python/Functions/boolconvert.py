#!/usr/bin/python3
# boolconvert.py
'''Boolean converter'''
__author__ = "Richard li"
__version__ = "1.0"


def convert(response):
    """determines if the string given means

    :param: response: a string variation of yes or no
    :return: True if statement is in agreeance, False if not"""

    if response == "yes" or response == "yah" or response == "YES" \
            or response == "Yes" or response == "Ya" or response == "yeah":
        return True
    return False
