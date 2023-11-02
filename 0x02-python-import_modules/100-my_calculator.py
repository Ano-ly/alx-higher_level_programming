#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    argv = sys.argv
    op_list = ('+', '-', '*', '/')
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    if argv[2] == '-':
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    if argv[2] == '*':
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    if argv[2] == '/':
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
