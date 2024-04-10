import math

class BST_Node:
    val = None
    left = None
    right = None
    parent = None
    
    def __init__(self, val = None):
        self.val = val


    def insert(self, val):
        if self.val is None:
            self.val = val 
            return 
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BST_Node(val)
            self.left.parent = self
        else:
            if self.right:
                self.right.insert(val)
                return 
            self.right = BST_Node(val)
            self.right.parent = self

def right_rotate(node):
    parent = node.parent
    left = node.left
    left_right = left.right 

    if parent: 
        if parent.left == node:
            parent.left = left
        else:
            parent.right = left
    else:
        left.parent = None
        node.parent = left

    left.parent = parent

    left.right = node
    node.parent = left

    node.left = left_right
    if left_right:
        left_right.parent = node


def left_rotate(node):
    parent = node.parent
    right = node.right
    right_left = right.left

    if parent:
        if parent.right == node:
            parent.right = right
        else:
            parent.left = right
    else:
        right.parent = None
        node.parent = right

    right.parent = parent

    right.left = node
    node.parent = right

    node.right = right_left
    if right_left:
        right_left.parent = node


def bst_to_vine(root):
    count = 0
    rotator =  root
    while rotator:
        if rotator.left:
            right_rotate(rotator)
            rotator = rotator.parent
        else:
            count += 1
            rotator = rotator.right 
    
    return count


def calculate_height(tree):
    if tree is not None:
        return nheight(tree, 0)
    else:
        return 0
    
def nheight(tree, h):
    if tree is None:
        return h 
    
    left_height = nheight(tree.left, h+1)
    right_height = nheight(tree.right, h+1)

    return max(left_height, right_height)

def to_root(tree_node: BST_Node):
    node = tree_node

    while node.parent:
        node = node.parent

    return node 


def compress(node: BST_Node, count: int):
    for i in range(count):
        left_rotate(node)
        node = node.parent.right

def dsw(root: BST_Node):
    size = bst_to_vine(root)
    
    h = math.floor((math.log2(size + 1)))
    m = int(math.pow(2, h)) - 1

    compress(to_root(root), size - m)

    while m > 1:
        m //= 2
        compress(to_root(root), m)
def print_tree_preorder(node):
    if node is None:
        return
    print(node.val,end=" -> ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

if __name__ == '__main__':

    A = [7,2,1,6,4,3,5,12,8,13,10,9,11]
    root = BST_Node()
    for a in A:
        root.insert(a)

    dsw(to_root(root))
    print_tree_preorder(to_root(root))

