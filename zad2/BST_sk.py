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


    def print_preorder(self):
        if self.val is not None:
            print(self.val)
        if self.left is not None:
            self.left.print_preorder()
        if self.right is not None:
            self.right.print_preorder()


def right_rotate(node: BST_Node):
    parent = node.parent
    left = node.left
    left_right = left.right 

    if parent: # update parents if node is a child
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


def left_rotate(node: BST_Node):
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


def bst_to_vine(root: BST_Node):
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


def print_tree(tree):
    content='\n' # to hold final string
    cur_nodes=[tree] # all nodes at current level
    cur_height=calculate_height(tree) # height of nodes at current level
    sep=' '*(2**(cur_height-1)) # variable sized separator between elements
    while True:
        cur_height+=-1 # decrement current height
        if len(cur_nodes)==0: break
        cur_row=' '
        next_row=''
        next_nodes=[]

        if all(n is None for n in cur_nodes):
            break

        for n in cur_nodes:

            if n==None:
                cur_row+='   '+sep
                next_row+='   '+sep
                next_nodes.extend([None,None])
                continue

            if n.val!=None:       
                buf=' '*int((5-len(str(n.val)))/2)
                cur_row+='%s%s%s'%(buf,str(n.val),buf)+sep
            else:
                cur_row+=' '*5+sep

            if n.left!=None:  
                next_nodes.append(n.left)
                next_row+=' /'+sep
            else:
                next_row+='  '+sep
                next_nodes.append(None)

            if n.right!=None: 
                next_nodes.append(n.right)
                next_row+='\ '+sep
            else:
                next_row+='  '+sep
                next_nodes.append(None)

        content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
        cur_nodes=next_nodes
        sep=' '*int(len(sep)/2) # cut separator size in half
    
    print(content)


def to_root(tree_node: BST_Node):
    node = tree_node

    while node.parent:
        node = node.parent

    return node 


def compress(node: BST_Node, count: int):
    for i in range(count):
        left_rotate(node)
        # print(f'Compress {i+1}')
        # print_tree(to_root(node))
        node = node.parent.right

def dsw(root: BST_Node):
    size = bst_to_vine(root)
    
    h = math.floor((math.log2(size + 1)))
    m = int(math.pow(2, h)) - 1

    compress(to_root(root), size - m)

    while m > 1:
        m //= 2
        compress(to_root(root), m)


if __name__ == '__main__':
    data = [10,9,8,7,6,5,4,3,2,1]

    root = BST_Node()

    for val in data:
        root.insert(val)

    dsw(to_root(root))
    print_tree(to_root(root))

