#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    resList = []
    resList.append(list(map((number).__mul__, my_list)))
    return (resList[0])
