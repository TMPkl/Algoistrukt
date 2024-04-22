import math
import random
import timeit
import sys
import sys
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

def genD(n):
    D = [random.randrange(0,n*10,1) for _ in range(n)]
    D.sort(reverse=True)
    f=open("test_data_D.txt","w")
    f.write(str(D)[1:-1])
    f.close()
    return D

if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    # for n in range(10,10001,1000):
    #     D = genD(n)
    #     root = BST_Node()
    #     for d in D:
    #         root.insert(d)
    #     start = timeit.default_timer()
    #     dsw(to_root(root))
    #     stop = timeit.default_timer()
    #     print(f'N = {n}, Time = {stop - start}')
    for n in range(1000,10001,1000):
        print(str(n),end = ";")
        for _ in range(10):
            A = genD(n)

            root = BST_Node()
            
            for a in A:
                root.insert(a)
            t0 = timeit.default_timer()
            dsw(to_root(root))
            t1 = timeit.default_timer()
            t = t1-t0
            print(round(t,6),end=";")
        print()
        