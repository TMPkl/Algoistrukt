import math

class BST:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False

def insert(node, key):
    if node is None:
        return BST(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def print_tree_preorder(node):
    if node is None:
        return
    print(node.key,end=" -> ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

def right_full_rotation(node, parent=None):
    while node is not None:
        if node.left is None:
            if node.right is not None:
                right_full_rotation(node.right, node)
            break
        else:
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            if parent:
                if parent.left == node:
                    parent.left = new_root
                else:
                    parent.right = new_root
            node = new_root
    if parent is None:
        return node 
    else:
        return None


def left_rotate(node, parent):
    if node is None or node.right is None:
        return node

    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    
    if parent:
        if parent.left == node:
            parent.left = new_root
        else:
            parent.right = new_root
    
    return new_root

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def balance_tree(node):
    n = count_nodes(node)
    m = 2 ** (int(math.log2(n + 1))) - 1
    node = perform_rotations(node, n - m)
    node = perform_rotations(node, m)
    return node

def perform_rotations(node, m):
    while m > 1:
        m = m // 2
        current = node
        parent = None
        for _ in range(m):
            if current is None: 
                break
            parent = current
            current = left_rotate(current, parent) if _ % 2 == 0 else right_full_rotation(current, parent)
            current = current.right if _ % 2 == 0 else current.left
        node = current
    return node


A = [6,3,1,5,4,2]

root = None
for a in A:
    root = insert(root, a)

print_tree_preorder(root)
print()
root = right_full_rotation(root)
print_tree_preorder(root)
root = balance_tree(root)
print()
print_tree_preorder(root)
