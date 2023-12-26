#!/usr/bin/python3

"""This contains the classes Node and SinglyLinkedList"""


class Node:
    """This class is the class Node."""

    def __init__(self, data, next_node=None):
        """This function initialises the class instance"""

        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is not None) and (type(value) is not Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value


class SinglyLinkedList:
    """This class defines a singly-linked list"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a node in a SinglyLinkedList instance

        Args:

           value: value to be data in the inserted node

        """
        new_node = Node(value)
        iter = self.head
        if iter is None:
            self.head = new_node
        elif iter.data >= value:
            new_node.next_node = iter
            self.head = new_node
        else:
            if iter.next_node is None:
                iter.next_node = new_node
            else:
                while (iter.next_node) and (iter.next_node).data < value:
                    iter = iter.next_node
                new_node.next_node = iter.next_node
                iter.next_node = new_node

    def __str__(self):
        """Prints string representation of class instance"""

        linked_list = []
        iter = self.head
        while iter is not None:
            linked_list.append(str(iter.data))
            iter = iter.next_node
        return ("\n".join(linked_list))
