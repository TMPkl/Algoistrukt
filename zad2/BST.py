class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return BST(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    return node

A = [8,11,2,52,0,4,6,5]

root = None
for a in A:
    root = insert(root, a)


def find_smallest(node):
    if node.left is None:
        print(node.key)
        return node.key
    else:
        print(node.key,end="-->")
        find_smallest(node.left)

def find_largest(node):
    if node.right is None:
        print(node.key)
        return node.key
    else:
        print(node.key,end="-->")
        return find_largest(node.right)



def print_tree_preorder(node):
    if node is None:
        return
    print(node.key)
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

print_tree_preorder(root)
print("##################################################")
find_smallest(root)
print("##################################################")
find_largest(root)