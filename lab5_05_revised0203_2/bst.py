"""Module for BST
CPE202

Contains the data definition of BST,
and functions (not class member methods) on BST.

Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.


Author: Richard Hua
    Section: CPE202-05
    Winter 2020
"""
class BSTNode:
    """None or Node of Binary Search Tree. Contains key-value pairs.
    Attributes:
        key (any): key of node
        val (any): val of node
        left (BSTNode): left child
        right (BSTNode): right child
    """
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, BSTNode)\
        and self.key == other.key\
        and self.val == other.val\
        and self.left == other.left\
        and self.right == other.right

    def __repr__(self):
        return "BSTNode(k=%s, v=%s, left=%s, right=%s)"\
        % (self.key, self.val, self.left, self.right)
    #---- to do ----
    # implement __eq__ and __repr__
    #---------------

#---- to do ----
# implement the following recursive funstions
# write a docstring for each function
#
def get(tree, key):
    """Returns the value at a key in the tree
    Args:
        tree (BSTNode): the root of TreeMap
        key (any): key to retrieve value from
    Returns:
        any: the value associated with the key
    """
    if tree is None:
        return None
    if key == tree.key:
        return tree.val
    elif key < tree.key:
        value = get(tree.left, key)
    else: # key > tree.key
        value = get(tree.right, key)
    return value

def get_root_key(tree):
    """Returns the root key
    Args:
        tree (BSTNode): the root of TreeMap
    Returns:
        any: the key of root node
    """
    if tree:
        return tree.key
    return None

def contains(tree, key):
    """ Checks to see if the tree contains the given key.
    Args:
        tree (BSTNode): the root of TreeMap
        key (any): key for checking existence
    Returns:
        bool: True if key exists, otherwise False.
    """
    if tree is None:
        return False
    if key == tree.key:
        return True
    elif key < tree.key:
        # REMEMBER TO SAVE THE RETURN
        inTree = contains(tree.left, key)
    else: # key > tree.key
        inTree = contains(tree.right, key)
    return inTree # THEN RETURN BACK TO CALLER (LAB5 OR TESTS)

def insert(tree, key, val):
    """Takes a key and inserts its value into the BST.
    Args:
        tree (BSTNode): the root of the BST tree/subtree
        key (any): the key for insertion
        val (any): the value to be inserted
    Returns:
        BSTNode: root node
    """
    if tree is None:
        return BSTNode(key, val, None, None)
    if key == tree.key:
        tree.val = val
    elif key < tree.key:
        tree.left = insert(tree.left, key, val)
    else: # key > tree.key
        tree.right = insert(tree.right, key, val)
    return tree

def delete(tree, key):
    """delete a given item in the tree
    Args:
        tree (BSTNode): the root of the BST tree/subtree
        key (any): the item to be deleted
    Returns:
        BSTNode: the root of a BinarySearchTree
    Raises:
        KeyError : raised if tree is None or item not found
    """
    # Case 1 : Empty Tree
    if tree is None:
        raise KeyError("%s not found! Tree is empty")
    # Case 2 : item not in tree
    if not contains(tree, key):
        raise KeyError
    if tree.key == key: # When we find the node to delete
        # Case 3 : no children
        if not (tree.left or tree.right):
            tree = None
            return tree
        # Case 4 : node has two children
        elif tree.left and tree.right:
            smallest = smallest_of_right_subtree(tree.right)
            tree.key = smallest.key
            tree.val = smallest.val
            if tree.right == smallest: # if smallest is del.right's node
                # adopt small's right subtree (Node or None)
                tree.right = smallest.right
            return tree
        # Case 4 : Only left child exists
        elif tree.left:
            return tree.left
        # Case 5 : Only right child exists
        else:
            return tree.right
    elif tree.key < key: #traverse right subtree
        right_sub = delete(tree.right, key)
        tree.right = right_sub # link parent to del's child
        return tree
    else: #traverse left subtree
        left_sub = delete(tree.left, key)
        tree.left = left_sub
        return tree

def smallest_of_right_subtree(tree):
    if tree.left is None:
        return tree
    smallest = smallest_of_right_subtree(tree.left)
    # No left child since already smallest. Check right.
    tree.left = smallest.right #builds smallest's right subtree links
    return smallest


def find_min(tree):
    """Finds the minimum in the BST. (Lowest left node)
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        key (any): the key of min value
        val (any): the minimum value
    """
    if tree is None:
        return None, None
    if tree.left is None:
        key = tree.key
        val = tree.val
        return key, val
    return find_min(tree.left)

def find_max(tree):
    """Finds the maximum value in the BST. Lowest right node.
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        key (any): the key of max value
        val (any): the max value
    """
    if tree is None:
        return None, None
    if tree.right is None:
        key = tree.key
        val = tree.val
        return key, val
    return find_max(tree.right)

def inorder_list(tree):
    """Traverses BST inorder and saves the keys in a list.
    Left -> Root -> Right
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        list: list of BST keys representing inorder traversal
    """
    root = get_root_key(tree)
    # must create empty list here, or else list will be appended to
    # previous list every other time inorder_list is called
    return inorder_list_helper(tree, root, lst=[])

def inorder_list_helper(tree, root, lst):
    """Helper to traverses BST inorder and save the keys in a list.
    Left -> Root -> Right
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        list: list of BST keys representing inorder traversal
    """
    if tree is None: # make sure list exists before attempting to access attr
        return
    inorder_list_helper(tree.left, root, lst) # go to left subtree
    lst.append(tree.key) # returning to subroot after hitting none on subtree
    inorder_list_helper(tree.right, root, lst) # go to right subtree
    if tree.key == root: # return finished list if back to top root node
        return lst

def preorder_list(tree):
    """Preorder traversal of BST keys saved to a list.
    Root -> Left -> Right
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        list: list of BST keys representing inorder traversal
    """
    root = get_root_key(tree)
    return preorder_list_helper(tree, root, lst=[])

def preorder_list_helper(tree, root, lst):
    """Helper to preorder traverse BST and save the keys to a list.
    Root -> Left -> Right
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        list: list of BST keys representing preorder traversal
    """
    if tree is None: # make sure list exists before attempting to access attr
        return
    lst.append(tree.key) # store curr node value in list
    preorder_list_helper(tree.left, root, lst) # go to left subtree
    preorder_list_helper(tree.right, root, lst) # go to right subtree
    if tree.key == root: # return finished list if back to top root node
        return lst

def tree_height(tree):
    """Gives the height of the tree. Defined as number of edges
    from the root. (i.e. root is height = 0)
    Args:
        tree (BSTNode): the root of the BST tree/subtree
    Returns:
        int: height of tree
    """
    if tree is None:
        return None
    # left and right children exist
    if tree.left and tree.right:
        return 1 + max(tree_height(tree.left), tree_height(tree.right))
    # First case already failed. One or less children.
    elif tree.left:
        return 1 + tree_height(tree.left)
    elif tree.right:
        return 1 + tree_height(tree.right)
    else:
        return 0

def range_search(tree, min, max):
    """Returns a list of values that fall within given range.
    Max of range excluded. i.e range = [min, max)
    Min and max are keys. List returned are respective values.
    Args:
        min (int): low end of range, value is inclusive in range
        max (int): max end of range, value is exclusive in range
    Returns:
        list: values within range of [min, max)
    """
    if tree is None:
        return None
    vals = []
    list = inorder_list(tree) #keys of BST in ascending order
    for key in list:
        if key >= min and key < max: # rmbr to use AND not OR
            vals.append(get(tree, key))
    return vals
