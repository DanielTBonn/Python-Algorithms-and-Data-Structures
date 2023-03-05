from pythonds3.basic import Stack
from random import randrange
class HeaderNode:
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value

    @property
    def down(self):
        return self._down
    
    @down.setter
    def down(self, value):
        self._down = value

class DataNode:
    def __init__(self, key, value):
        self._key = key
        self._data = value
        self._next = None
        self._down = None

    @property
    def key(self):
        return self._key
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next= value

    @property
    def down(self):
        return self._down
    
    @down.setter
    def down(self, value):
        self._down = value

class SkipList:
    def __init__(self):
        self._head = None

    def search(self, key):
        current = self._head
        while current:
            if current.next is None:
                current = current.down
            else:
                if current.next.key == key:
                    return current.next.data
                if key < current.next.key:
                    current = current.down
                else:
                    current = current.next
        return None

    def insert(self, key, value):
        if self._head is None:
            self._head = HeaderNode()
            temp = DataNode(key, value)
            self._head.next = temp
            top = temp
            while randrange(2) == 1:
                newhead = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                newhead.next = temp
                newhead.down = self._head
                self._head = newhead
                top = temp
        else:
            tower = Stack()
            current = self._head
            while current:
                if current.next is None:
                    tower.push(current)
                    current = current.down
                else:
                    if current.next.key > key:
                        tower.push(current)
                        current = current.down
                    else:
                        current = current.next

            lowest_level = tower.pop()
            temp = DataNode(key, value)
            temp.next = lowest_level.next
            lowest_level.next = temp
            top = temp
            while randrange(2) == 1:
                if tower.is_empty():
                    newhead = HeaderNode()
                    temp = DataNode(key, value)
                    temp.down = top 
                    newhead.next = temp
                    newhead.down = self._head
                    self._head = newhead
                    top = temp
                else:
                    next_level = tower.pop()
                    temp = DataNode(key, value)
                    temp.down = top
                    temp.next = next_level.next
                    next_level.next = temp
                    top = temp
    
    # Implements the delete method (assuming the key is present)
    def __delitem__(self, key):
        
        # create a stack of every instance of current where current.next.key == key, we use these points to cut out the key we wish to delete
        tower = Stack()
        current = self._head

        # search for every instance of the key and push the found keys previous node to the stack and set current to current.down
        while current:
            if current.next is None:
                current = current.down
            else:
                if current.next.key == key:
                    tower.push(current)
                    current = current.down
                elif key < current.next.key:
                    current = current.down
                else:
                    current = current.next

        # here we will create a while loop to cut out the key
        while not tower.is_empty():
            current = tower.pop()

            temp = current.next
            current.next = temp.next    
    
    # Returns a boolean result if a key is present or not
    def __contains__(self, key):
        return self.search(key)
    
    # Return a list of keys in the map
    def keys(self):
        keys_list = []
        current = self._head
        while current.down:
            current = current.down

        while current.next:
            keys_list.append(current.next.key)
            current = current.next

        return keys_list
        
    
    # Return a list of values in the map
    def values(self):
        values_list = []
        for key in self.keys():
            values_list.append(self.search(key))
        return values_list
            
    
    # Returns the value related to a key
    def __getitem__(self, key):
        return self.search(key)

    # Sets the value of an item with a key
    def __setitem__(self, key, value):
        self.insert(key, value)
        

class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def get(self, key):
        return self.collection.search(key)
    


