from BinarySearchTree import BinarySearchTree, TreeNode

class AVLTreeNode(TreeNode):
        def __init__(self, key, value, left=None, right=None, parent=None):
            super().__init__(key, value, left=None, right=None, parent=None)
            self.key = key
            self.value = value
            self.left_child = left
            self.right_child = right
            self.parent = parent
            self.balance_factor = 0

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = AVLTreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.left_child)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)    

    def rotate_left(self, rotation_root):
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)
        )

    def rotate_right(self, rotation_root):
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor - 1 + min(0, new_root.balance_factor)
        )
        new_root.balance_factor = (
            new_root.balance_factor - 1 - max(rotation_root.balance_factor, 0)
        )

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                parent = node_to_remove.parent
                self._delete(node_to_remove)
                self.size = self.size - 1
                self.update_balance(parent)
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")


def tree_traversal(tree):

    if tree:
        tree_traversal(tree.left_child)
        print(tree.key)
        tree_traversal(tree.right_child)

my_tree = AVLTree()

my_tree['t'] = 'the'
my_tree['j'] = 'java'
my_tree['w'] = 'world'
my_tree['i'] = 'is'
my_tree['h'] = 'hello'
my_tree['b'] = 'bad'
my_tree['d'] = 'do'

my_tree['r'] = 'right'
my_tree['x'] = 'xylophone'

del my_tree['x']
del my_tree['r']

my_tree['r'] = 'right'
my_tree['x'] = 'xylophone'
my_tree['z'] = 'zebra'
my_tree['f'] = 'faucet'

tree_traversal(my_tree.root)

