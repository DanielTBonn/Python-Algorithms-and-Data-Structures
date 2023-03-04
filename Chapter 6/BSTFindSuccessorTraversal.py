from BinarySearchTree import BinarySearchTree

# Function using the find_successor() method to perform an inorder traversl of a BST. 
def successor_traversal(tree):
    current_node = tree.root.find_min() # Set current node to the smallest value in the tree.
    print(current_node.key) # Prints the smallest node
    while current_node.find_successor(): # Ends loop if current node has no successor/is the largest value in the tree
        current_node = current_node.find_successor() # Grabs next successor
        print(current_node.key) # Prints successor
        


def main():
    my_tree = BinarySearchTree()

    my_tree["a"] = "a"
    my_tree["q"] = "quick"
    my_tree["b"] = "brown"
    my_tree["f"] = "fox"
    my_tree["j"] = "jumps"
    my_tree["o"] = "over"
    my_tree["t"] = "the"
    my_tree["l"] = "lazy"
    my_tree["d"] = "dog" 

    successor_traversal(my_tree)


if __name__ == '__main__':
    main()
