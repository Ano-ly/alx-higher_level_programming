#!/usr/bin/python3
def safe_print_integer(value):
    """
    This function printsan integer value

        Args:

            value: value to be printed
    """
    if value is None:
        return (False)
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
