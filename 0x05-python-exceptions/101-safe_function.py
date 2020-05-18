#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        a = None
    return (a)
