from math import floor
from mimetypes import init  
class MinHeap():
    def __init__(self, size) -> None:
        self._size = size
        self._heap = [False for x in range(size)]
    
    def getChildren(self, index):
        return (2*index+1, 2*index+2)
    
    def getParent(self, index):
        return floor((index-1)/2)
    
    def add(self, data):
        """ Adds a new element to the heap. """
        data_index = self._size-1
        self._heap[data_index] = data
        parent_index = self.getParent(data_index)
        parent = self._heap[parent_index]
        while (parent == False or parent > data):
            self._heap[parent_index] = data
            self._heap[data_index] = parent
            data_index = parent_index
            parent_index = self.getParent(data_index)
            parent = self._heap[parent_index]
    
    def pop(self):
        """ Pops the element from the top of the heap. """
        popped = self._heap[0]
        (self._heap[0], self._heap[self._size-1]) = (self._heap[self._size - 1], self._heap[0])
        self._heap[self._size - 1] = False
        item_index = 0

        (left_index, right_index) = self.getChildren(item_index)
        (left, right) = (self._heap[left_index], self._heap[right_index])
        parent = self._heap[item_index]
        while(left < parent or right < parent):
            if(left < parent):
                (self._heap[parent], self._heap[left_index]) = (left,parent)
                item_index = left_index
                parent = left 
            else:
                (self._heap[parent], self._heap[right_index]) = (right,parent)
                item_index = right_index
                parent = right
            (left_index, right_index) = self.getChildren(item_index)
            (left, right) = (self._heap[left_index], self._heap[right_index])
        return popped 

