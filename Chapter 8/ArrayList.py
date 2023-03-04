class ArrayList:
    def __init__(self):
        self.size_exponent = 0
        self.max_size = 0
        self.last_index = 0
        self.my_array = []

    def append(self, val):
        if self.last_index > self.max_size - 1: 
            self.__resize()
        self.my_array[self.last_index] = val
        self.last_index += 1

    def __resize(self):
        new_size = 2 ** self.size_exponent
        print("new_size = ", new_size)
        new_array = [0] * new_size
        for i in range(self.max_size):
            new_array[i] = self.my_array[i]
        
        self.max_size = new_size
        self.my_array = new_array
        self.size_exponent += 1

    def __getitem__(self, idx):
        if idx < self.last_index:
            return self.my_array[idx]
        raise LookupError("index out of bounds")
    
    def __setitem__(self, idx, val):
        if idx < self.last_index:
            self.my_array[idx] = val
        raise LookupError("index out of bounds")
    
    def insert(self, idx, val):
        if self.last_index > self.max_size - 1:
            self.__resize()
        for i in range(self.last_index, idx - 1, -1):
            self.my_array[i + 1] = self.my_array[i]
        self.last_index += 1
        self.my_array[idx] = val

    def __str__(self):
        result = '['
        if self.last_index == 0:
            return '[]'
        for idx in range(self.last_index - 1):
            result += str(self.my_array[idx]) + ', '
        result += str(self.my_array[self.last_index - 1] )+ ']'
        return result

    # Deletes the item at the given index from the list
    def __delitem__(self, idx):
        if self.last_index <= abs(idx):
            raise LookupError("index out of bounds")
        for i in range(idx, self.last_index - 1):
            self.my_array[i] = self.my_array[i + 1]
        self.my_array[self.last_index - 1] = 0
        self.last_index -= 1
        
    
    # Removes and returns an item in the list. If an index isn't specified the default is the last item in the list.
    def pop(self, idx = -1):
        if idx == -1:
            val = self.my_array[self.last_index - 1]
            self.__delitem__(self.last_index - 1)
            return val
        val = self.my_array[idx]
        self.__delitem__(idx)
        return val
        

    # Searches for a given value and either returns its position if found, or -1 if not. 
    def index(self, val):
        idx = -1
        for i in range(self.last_index):
            if self.my_array[i] == val:
                idx = i
        return idx

    # Creates an iterator for the list
    def __iter__(self):
        return iter(self.my_array[0:self.last_index])
    
    # Implements the + operator for concatenating ArrayList type objects
    def __add__(self, array):
        if type(array) == type(self):
            for item in array:
                self.append(item)
        else:
            raise TypeError('cannot concatenate non-ArrayList object')
        return self
    
    # Implements the * operator for creating multiples of an ArrayList type object and concatenating to the end of the ArrayList.
    def __mul__(self, mult):
        if not int(mult):
            raise TypeError('can only multiply integers')
        temp = self.my_array[:self.last_index]
        for i in range(mult - 1):
            for item in temp:
                self.append(item)
        print(temp)
        return self



def main():
    a = ArrayList()
    n = 4
    for i in range(1, n):
        a.append(i)
    #del a[1]
    #print(a)
    #print(a.pop())
    #print(a.index(0))
    #print(a)
    #print(a.my_array)
    #print(a.last_index)
    #print(iter(a))
    #for val in a:
    #    print(val)

    b = ArrayList()
    for i in range(4,10):
        b.append(i)

    a = a + b
    print(a)
    a = a * 5
    print(a)
main()
#lst = [1,2,3]
