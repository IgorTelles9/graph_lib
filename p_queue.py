from math import floor 

class PQueue():
    def __init__(self, size) -> None:
        self._size  = size
        self._heap = [ [index, float('inf')] for index in range(self._size) ]
        self._indices = [i for i in range(self._size)]

    def getChildren(self, index):
        (l,r) = (2*index+1, 2*index+2)
        if (l > self._size - 1):
            l = None
        if (r > self._size - 1):
            r = None
        return (l,r)

    def getParent(self, index):
        if (index == 0):
            return None
        return floor((index-1)/2)

    def getSize(self):
        return self._size 

    def getWeight(self, index):
        return self._heap[index][1]

    def pop(self):
        """ Pops out the first element of the queue """
        popped = self._heap[0][0]
        (self._heap[0], self._heap[self._size-1]) = (self._heap[self._size-1], self._heap[0])
        self._heap[self._size-1] = None
        (self._indices[0], self._indices[self._size-1]) = (self._indices[self._size-1], self._indices[0])
        self._size -= 1

        if(self._size > 0):
            self.update(self._heap[0][0], self._heap[0][1])

        return popped

    def update(self, data, weight):
        """ Given a data, updates its weight """
        index = self._indices.index(data)
        self._heap[index][1] = weight
        parent_index = self.getParent(index)
        (left_index, right_index) = self.getChildren(index)

        while (
            (parent_index != None and self._heap[parent_index][1] > self._heap[index][1]) or
            (left_index != None and self._heap[left_index][1] < self._heap[index][1]) or 
            (right_index != None and self._heap[right_index][1] < self._heap[index][1]) 
            ):

            if (parent_index != None and self._heap[parent_index][1] > self._heap[index][1]):

                (self._heap[parent_index], self._heap[index]) = (self._heap[index], self._heap[parent_index])
                (self._indices[parent_index], self._indices[index]) = (self._indices[index], self._indices[parent_index])
                index = parent_index
                (left_index, right_index) = self.getChildren(index)
                parent_index = self.getParent(index)
            
            elif (
            left_index != None and self._heap[left_index][1] < self._heap[index][1]
            and right_index != None and self._heap[right_index][1] < self._heap[index][1]
            ):
                pass
                min_index = left_index
                if (self._heap[left_index][1] > self._heap[right_index][1]):
                    min_index = right_index
                (self._heap[min_index], self._heap[index]) = (self._heap[index], self._heap[min_index])
                (self._indices[min_index], self._indices[index]) = (self._indices[index], self._indices[min_index])
                index = min_index
                (left_index, right_index) = self.getChildren(index)
                parent_index = self.getParent(index)

            else:
                if(left_index != None and self._heap[left_index][1] < self._heap[index][1]):

                    (self._heap[left_index], self._heap[index]) = (self._heap[index], self._heap[left_index])
                    (self._indices[left_index], self._indices[index]) = (self._indices[index], self._indices[left_index])
                    index = left_index
                    (left_index, right_index) = self.getChildren(index)
                    parent_index = self.getParent(index)

                else:
                    (self._heap[right_index], self._heap[index]) = (self._heap[index], self._heap[right_index])
                    (self._indices[right_index], self._indices[index]) = (self._indices[index], self._indices[right_index])
                    index = right_index
                    (left_index, right_index) = self.getChildren(index)
                    parent_index = self.getParent(index)