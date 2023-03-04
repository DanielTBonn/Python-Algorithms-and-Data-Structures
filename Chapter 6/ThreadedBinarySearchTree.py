from BinarySearchTree import BinarySearchTree, TreeNode

class ThreadedBinarySearchTree(BinarySearchTree):

    def __init__(self):
        super().__init__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = ThreadedTreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = ThreadedTreeNode(
                    key, value, parent=current_node
                )
                current_node.successor = current_node.find_successor()
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = ThreadedTreeNode(
                    key, value, parent=current_node
                )
                current_node.successor = current_node.find_successor()

class ThreadedTreeNode(TreeNode):

    def __init__(self, key, value, left=None, right=None, parent=None):
        super().__init__(key, value, left=None, right=None, parent=None)
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.successor = None    
