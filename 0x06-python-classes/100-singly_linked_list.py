#!/usr/bin/python3
'''2 classes used to create a singly linked list'''

class Node:
    '''contains data and a pointer to the next node'''
    def __init__(self, data, next_node=None):
        '''initializes data and next_node'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''returns data'''
        return (self.__data)

    @data.setter
    def data(self, value):
        '''setter for data'''
        if (type(value) is not int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''Returns next node in list'''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        '''setter for next node'''
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    '''Contains a chain of linked nodes'''
    def __init__(self):
        '''Initialization of head'''
        self.__head = None

    def sorted_insert(self, value):
        '''inserts a node at a sorted position'''
        hare = self.__head
        tortoise = hare
        if (hare is None):
            self.__head = Node(value, None)
            return
        if (hare.data > value):
            self.__head = Node(value, hare)
            return
        while (hare is not None and hare.data < value):
            tortoise = hare
            hare = hare.next_node

        tortoise.next_node = Node(value, hare)

    def liststr(self):
        '''makes a string of the list to be returned'''
        res = []
        hare = self.__head
        if (hare is None):
            return ("")
        while (hare is not None):
            res.append(str(hare.data))
            if (hare.next_node is not None):
                res.append('\n')
            hare = hare.next_node
        return ("".join(res))

    def __repr__(self):
        '''Defines return value of class'''
        return (self.liststr())
