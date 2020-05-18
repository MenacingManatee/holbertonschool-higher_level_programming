#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(args[0], args[1])
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        a = None
    return (a)
