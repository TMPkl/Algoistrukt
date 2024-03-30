class BST:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.balance = None

    def insert(self, additives):
        if self.key is None:
            self.key = additives
            self.parent = None
            return
        elif self.key > additives:
            if self.left is None:
                self.left = BST(additives, parent=self)
            else:
                self.left.insert(additives)
        else:
            if self.right is None:
                self.right = BST(additives, parent=self)
            else:
                self.right.insert(additives)

    def left_rotate(self):
        new_root = self.right
        self.right = new_root.left
        if new_root.left:
            new_root.left.parent = self
        new_root.parent = self.parent
        if not self.parent:
            return new_root
        if self is self.parent.left:
            self.parent.left = new_root
        else:
            self.parent.right = new_root
        new_root.left = self
        self.parent = new_root
        return self  # Return self after rotation

def print_tree_preorder(node):
    if node is None:
        return
    print(node.key, end=" -> ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

root = BST(2)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(4)

print("Before left rotation:")
print_tree_preorder(root)
print()

# Perform left rotation on the node with key 5
root.right = root.right.left_rotate()

print("After left rotation:")
print_tree_preorder(root)
print()
