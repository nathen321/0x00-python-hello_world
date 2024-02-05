#!/usr/bin/python3
"""function that returns the list of available attributes"""

class MyList(list):
    """ subclass of list """

    def print_sorted(self):
        """
        print sorted list of element
        """

        print(sorted(self))
