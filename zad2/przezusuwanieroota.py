class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.root = key
        self.level = 0
        self.balance = 0

    def level_order_traversal(self):
        if not self.root:
            return []
        poziom = [self]
        leafs = []
        while poziom:
            nl = []
            for node in poziom:
                leafs .append(node.root)
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)

            poziom = nl

        return leafs

    def balancing(self):
        while True:
            flag = True
            nodes = self.level_order_traversal()
            for node in nodes:
                podejrzany = self.searching_for_node(node)
                if podejrzany.balance > 1 or podejrzany.balance < -1:
                    value = podejrzany.root
                    self.delete_node(value)
                    self.insert(value)
                    self.calculate_balance()
                    flag = False
                    break
            if flag:
                return

    def searching_for_node(self, value):
        if value == self.root:
            return self
        elif value < self.root and self.left:
            return self.left.searching_for_node(value)
        elif value > self.root and self.right:
            return self.right.searching_for_node(value)
        else:
            return None

    def delete_node(self, value):
        if value < self.root:
            if self.left:
                self.left = self.left.delete_node(value)
        elif value > self.root:
            if self.right:
                self.right = self.right.delete_node(value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.minimum_value_node(self.right)
            self.root = temp.root
            self.right = self.right.delete_node(temp.root)
        if self is not None:
            self.calculate_balance()
        return self


    def minimum_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert(self, value):
        if value < self.root:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
            else:
                self.right.insert(value)
        self.calculate_balance()

    def calculate_balance(self):
        if self is None:
            return 0
        left_height = self.left.calculate_balance() if self.left else -1
        right_height = self.right.calculate_balance() if self.right else -1
        self.balance = left_height - right_height
        return max(left_height, right_height) + 1
    def print_tree_preorder(self):
        if self is not None:
            print(self.root, end=" ")
            if self.left:
                self.left.print_tree_preorder()
            if self.right:
                self.right.print_tree_preorder()

A = [3,1,2]

root = Node(A.pop(0))
for a in A:
    root.insert(a)
root.print_tree_preorder()
print()
root.balancing()
root.print_tree_preorder()
