#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for i in range(0, int(x)):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except:
            pass
    print("")
    return (printed)
