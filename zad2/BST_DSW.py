class TreeNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return TreeNode(key)
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


     
A = [6,3,1,5,4,2]

root = None
for a in A:
    root = insert(root, a)

print_tree_preorder(root)
print()
rroot = right_full_rotation(root)
print_tree_preorder(rroot)
print()
