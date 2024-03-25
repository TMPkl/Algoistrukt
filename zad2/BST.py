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

A = [8,11,2,0,4,52,5,6]

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
    print(node.key,end=" -> ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

def print_tree_sorted(node):
    if node is None:
        return
    print_tree_sorted(node.left)
    print(node.key)
    print_tree_sorted(node.right)

def print_pre_subtree(node,key):
    if node is None:
        return
    if key == node.key:
        print_tree_preorder(node)
    else:
        print_pre_subtree(node.left,key)
        print_pre_subtree(node.right,key)

# print("print_tree_preorder","##################################################")
# print_tree_preorder(root)
# print("find_smallest","##################################################")
# find_smallest(root)
# print("find_largest","##################################################")
# find_largest(root)
# print("print_tree_sorted","##################################################")
# print(print_tree_sorted(root))
# print("print_subtree_preordered(root,key)","##################################################")    
#print_pre_subtree(root,2)