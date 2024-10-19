"""
Tree Data Structure:

A tree is a hierarchical data structure that consists of nodes connected by edges.

For example:

        A
      / | \
     B  C  D
    /       \
   E         H
  / \
 F   G


Key Terminology:

Node: Each node contains a unique value and may have zero or more child nodes.
      The topmost node of a tree is called the root node (A).
      Nodes with no children are called leaf nodes or terminal nodes (F, G, C and H).

Height: The height of a tree is defined as the number of nodes on the longest path from the root to a leaf node.
"""


class Node:
    """
    A basic node in a tree structure.
    Each node has a value and can have children nodes.
    """

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)  # The appended child will be a TREE


class Tree:
    """
    A general tree class with methods for adding nodes.
    """

    def __init__(self, root_node_value):
        """
        Initialize an empty tree.
        """
        self.root = Node(root_node_value)

    def get_node(self, value):
        """
        Returns a pointer to the Node object with the corresponding value
        """
        #self is the root of some tree.
        if self.root.value == value:
            return self
        # We are here if this tree node's value isn't the required value
        for child_Node in self.root.children:
            # self.root.children is a list of Node(s) in a tree.
            # Recursively iterate on them, "casting" each Node to a Tree for function continuation.
            child_tree = type(self)(-1)  # This Tree's initial value is irrelevant
            child_tree.root = child_Node  # Override child_tree's root attribute, to be this current Node.
            #if isinstance(child_tree,BinaryTree):

            parent_node = child_tree.get_node(value)  # go deeper into the tree, look for the parent node
            if parent_node is not None:
                # Return parent_node only if it represents an actual Tree.
                # Python will return None for no matches found
                return parent_node
        return None

    def add_node(self, value, parent):
        """
        Add a node to the tree. Add the node as a child of the parent.

        :param value: The node value.
        :param parent: The parent node value to which the new node should be added as a child.

        :return: a pointer to the node object
        """
        # Create the child Node to be inserted onto this Tree
        child_node = Node(value)
        # This method is based on get_node
        parent_node = self.get_node(parent)  # Find the parent node in the tree
        parent_node.root.add_child(child_node)
        return child_node

    def height(self):
        """
        Returns the height of the tree
        """
        if len(self.root.children) == 0:
            # This tree is a leaf
            return 1
        max_height = 1
        for child_Node in self.root.children:
            # self.root.children is a list of Node(s) in a tree.
            # Recursively iterate on them, "casting" each Node to a Tree for function continuation.
            child_tree = Tree(-1)  # This Tree's initial value is irrelevant
            child_tree.root = child_Node  # Override child_tree's root attribute, to be this current Node.

            branch_height = 1 + child_tree.height()
            if branch_height > max_height:
                max_height = branch_height
        return max_height


class BinaryTree(Tree):
    """
    A tree in which each node has at most two children, known as the left child and the right child.
    This class inheriting from the general tree class.

    You should raise an RuntimeError exception
    """
    last_change_cache = ('direction','parent')
    def __init__(self, root_node_value):
        super().__init__(root_node_value)
        self.has_left = False
        self.has_right = False

    def set_left_node(self, value, parent):
        """
        Sets a new left node for a given `parent` node value.
        Returns a pointer to the node
        """
        # Create the child tree node
        child_node = Node(value)

        # Find the parent node
        parent_node = self.get_node(parent)
        # Insert left_node at relevant position
        parent_node_children = parent_node.root.children
        if len(parent_node_children) > 0 and self.last_change_cache == ('left', parent):
            parent_node_children[0] = child_node
        else:
            parent_node_children.insert(0, child_node)
            parent_node.has_left = True
            self.last_change_cache = ('left', parent)
        return child_node

    def set_right_node(self, value, parent):
        # Create the child tree node
        child_node = Node(value)

        # Find the parent node
        parent_node = self.get_node(parent)
        # Insert left_node at relevant position
        parent_node_children = parent_node.root.children
        if len(parent_node_children) > 1: #and self.last_change_cache == ('right', parent):
            parent_node_children[-1] = child_node
        else:
            parent_node_children.insert(len(parent_node_children), child_node)
            parent_node.has_right = True
            #self.last_change_cache == ('right', parent)
        return child_node


if __name__ == "__main__":
    # Create tree
    #         A
    #       / | \
    #      B  C  D

    t = Tree('A')
    t.add_node('B', parent='A')
    t.add_node('C', parent='A')
    t.add_node('D', parent='A')

    # Create tree
    #         A
    #       / | \
    #      B  C  D
    #     /
    #    E

    t = Tree('A')
    t.add_node('B', parent='A')
    t.add_node('C', parent='A')
    t.add_node('D', parent='A')
    t.add_node('E', parent='B')
    print(t.height())
    # Create a binary tree
    #         A
    #       /   \
    #      B     C
    #     /     / \
    #    D     E   F
    bt = BinaryTree('A')
    bt.set_left_node('B', parent='A')
    bt.set_right_node('C', parent='A')
    bt.set_left_node('D', parent='B')
    bt.set_left_node('E', parent='C')
    bt.set_right_node('F', parent='C')
    bt.set_right_node('G', parent='C')  # set G as another right node of C should override the existed one, F
    print(bt.height())  # should be 3
