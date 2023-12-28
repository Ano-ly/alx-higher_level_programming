#!/usr/bin/python3
def safe_print_division(a, b):
    """This function prints the result of a division"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
