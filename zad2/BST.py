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

def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.key)
        result.extend(inorder_traversal(root.right))
    return result

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
def right_full_rotated(root):
    new_root = None
    D = inorder_traversal(root)
    for d in D:
        new_root = insert(new_root,d)
    return new_root

################
def compress_to_balanced_tree(root, size):
    if root is None:
        return None

    num_leaves = size + 1 - 2**((size+1).bit_length()-1)
    for _ in range(num_leaves):
        grandparent = root
        parent = root.right
        while parent.right is not None:
            grandparent = parent
            parent = parent.right
        grandparent.right = parent.left
        parent.left = grandparent
        root = parent
    while size > 1:
        size >>= 1
        grandparent = root
        parent = root.right
        for _ in range(size):
            child = parent.right
            grandparent.right = child
            parent.right = child.left
            child.left = parent
            grandparent = child
            parent = grandparent.right
        root = grandparent
    return root
################


A = [20,15,30,25,40,23,28]

root = None
for a in A:
    root = insert(root, a)

print_tree_preorder(root)
print()
root = right_full_rotated(root)
print("I stage DSW ")
print_tree_preorder(root)
print()
print("II stage DSW ")
root = compress_to_balanced_tree(root,len(A))
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