#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(args[0], args[1])
    except ZeroDivisionError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        a = None
    except IndexError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        a = None
    finally:
        return (a)
