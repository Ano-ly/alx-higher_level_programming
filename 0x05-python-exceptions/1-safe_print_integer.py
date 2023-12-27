#!/usr/bin/python3
def safe_print_integer(value):
    """
    This function printsan integer value

        Args:

            value: value to be printed
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
