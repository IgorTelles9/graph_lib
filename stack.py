from node import Node 

class Stack:
    """ A class which describes a stack. """
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """ Pushes data onto the top of the stack """
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """ Removes data on the top of the stack """
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        """ Peeks the top of the stack """
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")


    def __len__(self):
        """ Returns the size of the stack """
        return self._size

    def __repr__(self):
        """ Returns a printable representation of the stack """
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        """ Prints the stack """
        return self.__repr__()