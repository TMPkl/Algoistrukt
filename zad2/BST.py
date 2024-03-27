class BST:
    def __init__(self, key, left=None, right = None):
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




def find_smallest(node):
    if node.left is None:
        print(node.key)
        return node.key
    else:
        print(node.key, end="-->")
        return find_smallest(node.left)

def find_largest(node):
    if node.right is None:
        print(node.key)
        return node.key
    else:
        print(node.key, end="-->")
        return find_largest(node.right)




def print_tree_preorder(node):
    if node is None:
        return
    print(node.key,end=" -> ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.key)
        result.extend(inorder_traversal(root.right))
    return result

def print_tree_sorted(node):
    if node is None or node.key is None:
        return
    print_tree_sorted(node.left)
    if node.key is not None: 
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
def right_full_rotated(root):
    new_root = None
    D = inorder_traversal(root)
    for d in D:
        new_root = insert(new_root,d)
    return new_root

A = [20,5,3,6,21,23]

root = None
for a in A:
    root = insert(root, a)

print("print_tree_preorder","##################################################")
print_tree_preorder(root)
print()
print("find_smallest","##################################################")
find_smallest(root)
print("find_largest","##################################################")
find_largest(root)
print("print_tree_sorted","##################################################")
print_tree_sorted(root)
print("print_subtree_preordered(root,key)","##################################################")    
print_pre_subtree(root,21)