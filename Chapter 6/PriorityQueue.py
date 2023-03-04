from BinaryHeap import MinBinaryHeap

# Inheriting a MinBinaryHeap where the highest priority items are the lowest numbers.
class PriorityQueue(MinBinaryHeap):
    
    # Constructor
    def __init__(self):
        super().__init__()

    # Inserts and automatically orders items in the list
    def enqueue(self, item):
        self.insert(item)

    # Pops out the highest priority item in the list
    def dequeue(self):
        return self.delete()


def main():
    a_heap = PriorityQueue()
    a_heap.heapify([9, 5, 6, 2, 3])

    print(a_heap)
    a_heap.enqueue(10)
    print(a_heap)
    print(a_heap.dequeue())
    print(a_heap.dequeue())
    print(a_heap)
    a_heap.enqueue(12)
    print(a_heap)
    print(a_heap.dequeue())
    print(a_heap)

if __name__ == '__main__':
    main()
