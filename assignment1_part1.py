#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS-211 Week 1 Assignment Part 1"""


class ListDivideException(Exception):
    """Divide exception class"""
    pass


def listDivide(numbers, divide=2):
    """This function will divide each number in the list using the divider
    specified in the second parameter. It will return how many numbers in the
    list are divisble by the number.

    Args:
        numbers (list): First paramter should be a list of integers.
        divide (int, optional): The integer that will act as the divider.

    Returns:
        int: The return value should be the number of values successfully
            divisible by the divide parameter.
    """
    counter = 0
    for num in numbers:
        if num % divide == 0:
            counter += 1
    return counter


def testListDivide(test=None):
    """This function will test the listDivide() function. It verifies that
    the function is working as intended, otherwise it will raise an error.

    Args:
        test (list, optional): This should be a list of integers.

    Returns:
        AttributeError: If listDivide() function breaks, exception is raised."""
    if test is None:
        test = [[1, 2, 3, 4, 5],
                [2, 4, 6, 8, 10],
                [30, 54, 63, 98, 100],
                []]
        try:
            listDivide(test[0])
            listDivide(test[1])
            listDivide(test[2], 10)
            listDivide(test[3])
            listDivide(test[1], 1)
        except Exception:
            raise ListDivideException("One of the tests have failed.")
    else:
        try:
            listDivide(test)
        except Exception:
            raise ListDivideException("One of the tests have failed.")
    return


testListDivide()
