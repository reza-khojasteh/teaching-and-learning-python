# A program to find the inorder successor of a node in a BST
import queue


# A class to represent a BST
class BST:
    # A class to represent a node in a BST
    class Node:
        # Node's init function
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    # BST's init function
    def __init__(self):
        self.root = None

    # BST's insert function
    def insert(self, data):
        # If the tree is empty, create a new node as the root
        if self.root is None:
            self.root = BST.Node(data)
        # otherwise, find the right place to insert
        else:
            # curr points to the variable we are currently looking at
            curr = self.root
            inserted = False
            # Keep looping until we find the right place to insert
            while not inserted:
                # If the data is smaller than the current node's data, go left
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        inserted = True
                # otherwise, go right
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        inserted = True

    # BST's search function
    def search(self, data):
        curr = self.root

        while curr is not None:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr

        return None

    # BST's breadth first print function
    def breadth_first_print(self):
        the_nodes = queue.Queue()

        if self.root is not None:
            the_nodes.put(self.root)

        while not the_nodes.empty():
            curr = the_nodes.get()

            if curr.left:
                the_nodes.put(curr.left)
            if curr.right:
                the_nodes.put(curr.right)

            print(curr.data, end=" ")

    # BST's (wrapped) recursive search function
    def wrapped_recursive_search(self, data, subtree):
        # If the subtree is empty, return None
        if subtree is None:
            return None
        # otherwise, recursively search the subtree
        else:
            if data < subtree.data:
                return self.wrapped_recursive_search(data, subtree.left)
            elif data > subtree.data:
                return self.wrapped_recursive_search(data, subtree.right)
            else:
                return subtree

    # BST's (wrapper) recursive search function
    def recursive_search(self, data):
        return self.wrapped_recursive_search(data, self.root)

    # BST's (wrapped) recursive insert function
    def wrapped_recursive_insert(self, data, subtree):
        # If the subtree is empty, create a new node as the subtree
        if subtree is None:
            return BST.Node(data)
        elif data < subtree.data:
            subtree.left = self.wrapped_recursive_insert(data, subtree.left)
        else:
            subtree.right = self.wrapped_recursive_insert(data, subtree.right)
        return subtree

    # BST's (wrapper) recursive insert function
    def recursive_insert(self, data):
        self.root = self.wrapped_recursive_insert(data, self.root)

    # BST's (wrapped) recursive print_inorder function
    def print_inorder(self, subtree):
        if subtree is not None:
            self.print_inorder(subtree.left)
            print(subtree.data, end=" ")
            self.print_inorder(subtree.right)

    # BST's (wrapper) print function
    def print(self):
        self.print_inorder(self.root)  # or change to print_postorder or print_preorder
        print("")

    # BST's (wrapped) recursive print_preorder function
    def print_preorder(self, subtree):
        if subtree is not None:
            print(subtree.data, end=" ")
            self.print_preorder(subtree.left)
            self.print_preorder(subtree.right)

    # BST's (wrapped) recursive print_postorder function
    def print_postorder(self, subtree):
        if subtree is not None:
            self.print_postorder(subtree.left)
            self.print_postorder(subtree.right)
            print(subtree.data, end=" ")

    # BST's (wrapped) recursive print_recursive_between function
    def print_recursive_between(self, subtree, min, max):
        if subtree is None:
            return
        elif subtree.data < min:
            self.print_recursive_between(subtree.right, min, max)
        elif subtree.data > max:
            self.print_recursive_between(subtree.left, min, max)
        else:
            print(subtree.data)
            self.print_recursive_between(subtree.left, min, max)
            self.print_recursive_between(subtree.right, min, max)

    # BST's (wrapper) print_between function
    def print_between(self, min, max):
        self.print_recursive_between(self.root, min, max)

    # The following two could be applied on any binary trees in general:
    # BST's (wrapped) recursive_height function
    def recursive_height(self, subtree):
        if subtree is None:
            return 0
        else:
            return 1 + max(
                self.recursive_height(subtree.left),
                self.recursive_height(subtree.right),
            )

    # BST's (wrapper) height function
    def height(self):
        return self.recursive_height(self.root)

    # In a Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree.
    # Inorder Successor is None for the last node in Inorder traversal.
    # In a Binary Search Tree, Inorder Successor of an input node can also be defined as the node
    # with the smallest key greater than the key of the input node.

    # BST's (wrapped) recursive inorder_successor function
    # O(log(n)) Solution:
    def recursive_inorder_successor(self, subtree, value):
        if subtree is not None:
            print(subtree.data, end="->")

            if value >= subtree.data:
                result = self.recursive_inorder_successor(subtree.right, value)
                if result is not None:
                    return result
            else:
                result = self.recursive_inorder_successor(subtree.left, value)
                if result is not None:
                    return result

            if subtree.data > value:
                return subtree.data

    # BST's (wrapped) recursive inorder_successor function
    # O(n) Solution:
    def not_efficient_inorder_successor(self, subtree, value):
        if subtree is not None:
            print(subtree.data, end="->")

            result = self.not_efficient_inorder_successor(subtree.left, value)
            if result is not None:
                return result

            if subtree.data > value:
                return subtree.data

            result = self.not_efficient_inorder_successor(subtree.right, value)
            if result is not None:
                return result

    # BST's (wrapper) inorder_successor function
    def inorder_successor(self, value):
        node = self.search(value)

        if node is None:
            return None
        else:
            # return self.not_efficient_inorder_successor(self.root, value)
            return self.recursive_inorder_successor(self.root, value)

        # # And note why the following solution is wrong!!
        # node = self.search(value)
        #
        # if node is None or node.right is None:
        #     return None
        # else:
        #     node = node.right
        #
        #     while node.left is not None:
        #         node = node.left
        #
        #     return node.data


bst = BST()
# print(bst.root)

# bst.insert(2)
# bst.insert(1)
# bst.insert(3)
# print(bst.root.right.data)
# print(bst.search(3).data)
# bst.breadth_first_print()
# print(bst.recursive_search(4))

# bst.recursive_insert(3)
# bst.recursive_insert(1)
# bst.recursive_insert(2)
# bst.breadth_first_print()
# print(bst.recursive_search(3).data)
# bst.print()

# bst.print_between(1, 2)
# bst.print_between(1, 3)
# bst.print_between(1, 1)
# bst.print_between(3, 3)
# bst.print_between(2, 2)
# print(bst.height())

bst.recursive_insert(20)
bst.recursive_insert(8)
bst.recursive_insert(22)
bst.recursive_insert(4)
bst.recursive_insert(12)
bst.recursive_insert(10)
bst.recursive_insert(14)
print(bst.inorder_successor(14))
