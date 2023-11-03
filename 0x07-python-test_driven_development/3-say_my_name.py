#!/usr/bin/python3
""" defines function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints name (<first name> <last name>)

    Args:
        first_name (str): The fisrt name to be printed
        last_name (str): The last name to be printed

    Raises:
        TypeError: If either the first_name and last_name are not strings

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))
    