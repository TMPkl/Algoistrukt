import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_rotate(node):
    if node is None or node.left is None:
        return node
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root

def create_backbone(root):
    curr = root
    while curr:
        if curr.left:
            temp = curr.left
            curr.left = temp.right
            temp.right = curr
            curr = temp
        else:
            curr = curr.right
    return root

def create_balanced_tree(root, n):
    m = 2 ** int(math.log2(n + 1)) - 1  # Number of internal nodes in a complete binary tree
    balance = n - m
    for _ in range(balance):
        root = right_rotate(root)
        if root is None:
            return None
        root = root.right
    while m > 1:
        root = create_backbone(root)
        m //= 2
        for _ in range(m):
            root = right_rotate(root)
            if root is None:
                return None
            root = root.right
    return root

def balanceBST(root):
    # Count number of nodes in the tree
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    # Create backbone
    root = create_backbone(root)
    
    # Create balanced tree
    node_count = count_nodes(root)
    root = create_balanced_tree(root, node_count)

    return root

# Example usage:
# Assuming A is a global variable containing sorted values
A = [1, 2, 3, 4, 5, 6, 7]

def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

root = sorted_array_to_bst(A)
balanced_root = balanceBST(root)

# Function to traverse the tree (for testing purposes)
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.val, end=" -> ")
    inorder_traversal(node.right)

inorder_traversal(balanced_root)
