from structures.node import Node 

class Queue:
    """ A class which defines a queue. """
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, data):
        """ Pushes data into the end of the queue. """
        node = Node(data)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size += 1

    def pop(self):
        """ Removes the first node of the queue. """ 
        if self._size > 0:
            data = self.first.data
            self.first = self.first.next

            if self.first is None:
                self.last = None

            self._size -= 1
            return data
        raise IndexError("The queue is empty")

    def peek(self):
        """ Peeks the first element of the queue. """
        if self._size > 0:
            data = self.first.data
            return data
        raise IndexError("The queue is empty")


    def __len__(self):
        """ Returns its size """
        return self._size


    def __repr__(self):
        """ Returns a printable representation of the stack """
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        """ Prints the stack """
        return self.__repr__()