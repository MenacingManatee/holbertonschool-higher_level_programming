#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        res = True
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        res = False
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        res = False
    return (res)
