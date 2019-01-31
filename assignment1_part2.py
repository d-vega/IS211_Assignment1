#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS-211 Week 1 Assignment Part 2"""


class Book(object):
    """A Book friendly class that will format a book title and author into
    a structured sentence."""


    def __init__(self, author=None, title=None):
        """Constructor for Book

        Args:
            author (str): Name of book author should be a string.
            title (str): Name of book title should be a string."""
        self.author = author
        self.title = title


    def display(self):
        """Display title and author in formatted string.

        Returns:
            str: Output will return as a string. String will be a formatted
                sentence.

        Examples:
            >>> myinst = assignment1_part2.Book("John Steinbeck", "Of Mice and Men")
            >>> myinst.display()
            >>> Of Mice and Men, written by John Steinbeck"""
        info = "{t}, written by {a}".format(t=self.title, a=self.author)
        print info


RESULT1 = Book("John Steinbeck", "Of Mice and Men")
RESULT2 = Book("Harper Lee", "To Kill a Mockingbird")
RESULT1.display()
RESULT2.display()
