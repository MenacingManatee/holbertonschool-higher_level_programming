#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

op = "+-*/"
if sys.argv[2] not in op:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
print("{} {} {} = ".format(sys.argv[1], sys.argv[2], sys.argv[3]), end="")
ope = sys.argv[2]
a = int(sys.argv[1])
b = int(sys.argv[3])
if ope == '+':
    print("{}".format(add(a, b)))
elif ope == '-':
    print("{}".format(sub(a, b)))
elif ope == '*':
    print("{}".format(mul(a, b)))
else:
    print("{}".format(div(a, b)))
