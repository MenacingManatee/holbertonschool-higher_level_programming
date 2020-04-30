#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(38, 90, 21):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))


dis.dis(magic_calculation)
