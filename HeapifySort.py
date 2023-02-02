from BinaryHeap import MinBinaryHeap

def heapify_sort(a_list):

    a_heap = MinBinaryHeap()
    a_heap.heapify(a_list)
    new_list = []
    
    while not a_heap.is_empty():
        new_list.append(a_heap.delete())

    return new_list
    
def main():
    a_list = [10, 0, 8, 14, 18, 6, 9, 12, 7, 19] # Created a list of random integers in range 0, 20
    new_list = heapify_sort(a_list)
    print(new_list)

if __name__ == '__main__':
    main()