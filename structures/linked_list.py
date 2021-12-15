from structures.node import Node 

class LinkedList:
    """ A class which describes a linked list"""
    def __init__(self) -> None:
        self.head = None
        self._size = 0 
    
    def append(self, data):
        if self.head:
            n = self.head
            while (n.next):
                n = n.next
            n.next = Node(data)
        else:
            self.head = Node(data)
        self._size += 1

    def __len__(self):
        """ Returns the list size """
        return self._size
    
    def _getnode(self, index):
        """ A private method that returns a node given an index """
        n = self.head
        for i in range(index):
            if n:
                n = n.next
            else:
                raise IndexError("List index out of range") 
        return n

    def __getitem__(self, index):
        """ Returns the data of a node given its index """
        n = self._getnode(index)
        if n:
            return n.data
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, index, data):
        """ Sets the data of a node given its index """
        n = self._getnode(index)
        if n:
            n.data = data
        else:
            raise IndexError("List index out of range")

    def index(self, data):
        """Retorna o índice do data na lista"""
        n = self.head
        i = 0
        while(n):
            if n.data == data:
                return i
            n = n.next
            i = i+1
        raise ValueError("{} is not in list".format(data))

    def insert(self, index, data):
        """ Inserts a node in the index position """
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            n = self._getnode(index-1)
            node.next = n.next
            n.next = node
        self._size += 1

    def remove(self, data):
        """ Removes a node given its data """
        if self.head == None:
            raise ValueError("{} is not in list".format(data))
        elif self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            prev = self.head
            n = self.head.next
            while(n):
                if n.data == data:
                    prev.next = n.next
                    n.next = None
                    self._size -= 1
                    return True
                prev = n
                n = n.next
        raise ValueError("{} is not in list".format(data))

    def __repr__(self):
        r = ""
        n = self.head
        while(n):
            r = r + str(n.data) + "->"
            n = n.next
        return r

    def __str__(self):
        return self.__repr__() 
lista = LinkedList()
lista.append(1)
lista.append(2)
print(lista.head.data)
print(lista.head.next.data)
