#!/usr/bin/python3
'''Module describes a child of int that reverses '!=' and '==' '''


class MyInt(int):
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
