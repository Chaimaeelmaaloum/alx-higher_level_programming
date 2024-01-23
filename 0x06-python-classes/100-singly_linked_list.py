#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Node iner class"""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if (not isinstance(next_node, Node)) and (next_node is not None):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, next_node):
        if not isinstance(next_node, Node) and (next_node is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """singly_linked_list iner class"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        val = []
        tmp = self.__head
        while tmp is not None:
            val.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(val))

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None) and (tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
