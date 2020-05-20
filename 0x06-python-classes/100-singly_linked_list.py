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

    @property
    def next_node(self):
        '''Returns next node in list'''
        return (self.__next_node)

    @data.setter
    def data(self, value):
        '''setter for data'''
        if (not isinstance(value, int)):
            raise TypeError('data must be an integer')
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        '''setter for next node'''
        if not (isinstance(value, Node) or isinstance(value, None)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    '''Contains a chain of linked nodes'''
    def __init__(self):
        self.__head = None
        '''initialization'''
        pass

    def head(self, val):
        '''sets head to val'''
        self.__head = val

    def sorted_insert(self, value):
        '''inserts a node at a sorted position'''
        hare = self.__head
        tortoise = hare
        while (hare is not None and hare.data < value):
            tortoise = hare
            hare = hare.__next_node
        newNode = Node
        newNode.data = value
        newNode.__next_node = hare
        if (tortoise is not None):
            tortoise.__next_node = newNode
        else:
            self.__head = newNode

    def liststr(self):
        '''makes a string of the list to be returned'''
        res = []
        hare = self.__head
        while (hare is not None):
            res.append(hare.data)
            res.append('\n')
            hare = hare.__next_node
        return ("".join(res))

    def __repr__(self):
        '''Defines return value of class'''
        return (self.liststr())
