"""
Test Cases for bst and lab5 (TreeMap).
Checks class integrity and the associated methods
and functions.

Author: Richard Hua
Section: CPE202-05
Quarter: Winter 2020

"""

import unittest

import bst
from lab5 import TreeMap, import_classmates, search_classmate

class MyTest(unittest.TestCase):

    """
    TESTS FOR BST

                4
            2       5
         1    3        9
      0              6
                       7
                         8
    inorder: 0, 1, 2, 3, 4, 5,
    """


    def test_bst_insert(self):
        t = None
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        self.assertEqual(t.key, 4)

    def test_bst_get(self):
        t = None
        self.assertEqual(bst.get(t, 5), None)
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        self.assertEqual(bst.get(t, 4), 'four')
        self.assertEqual(bst.get(t, 2), 'two')

    def test_bst_contains(self):
        t = None
        # Empty tree
        self.assertFalse(bst.contains(t, 5))
        t = bst.insert(t, 4, 'four')
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        # Not Contained
        self.assertFalse(bst.contains(t, 44))
        # Contained
        self.assertTrue(bst.contains(t, 2))
        self.assertTrue(bst.contains(t, 8))

    def test_bst_find_min(self):
        t = None
        # Empty tree
        self.assertEqual(bst.find_min(t), (None, None))
        t = bst.insert(t, 2, 'two')
        # 1 Node
        self.assertEqual(bst.find_min(t), (2, 'two'))
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        # Finding min in populated list
        self.assertEqual(bst.find_min(t), (0, 'zero'))

    def test_bst_find_max(self):
        t = None
        # Empty tree
        self.assertEqual(bst.find_max(t), (None, None))
        t = bst.insert(t, 2, 'two')
        # 1 Node
        self.assertEqual(bst.find_max(t), (2, 'two'))
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        # Finding max in populated list
        self.assertEqual(bst.find_max(t), (9, 'nine'))

    def test_bst_inorder_list(self):
        t = None
        # Empty tree
        self.assertEqual(bst.inorder_list(t), None)
        # 1 Node
        t = bst.insert(t, 4, 'four')
        self.assertEqual(bst.inorder_list(t), [4])
        t = bst.insert(t, 2, 'two')
        # self.assertEqual(bst.find_max(t), (2, 'two'))
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        # List inorder from populated list
        self.assertEqual(bst.inorder_list(t), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bst_preorder_list(self):
        t = None
        # Empty tree
        self.assertEqual(bst.preorder_list(t), None)
        # 1 Node
        t = bst.insert(t, 4, 'four')
        self.assertEqual(bst.preorder_list(t), [4])
        t = bst.insert(t, 2, 'two')
        # self.assertEqual(bst.find_max(t), (2, 'two'))
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        # List inorder from populated list
        self.assertEqual(bst.preorder_list(t), [4, 2, 1, 0, 3, 5, 9, 6, 7, 8])

    def test_bst_tree_height(self):
        t = None
        # Empty tree
        self.assertEqual(bst.tree_height(t), None)
        # 1 Node
        t = bst.insert(t, 4, 'four')
        self.assertEqual(bst.tree_height(t), 0)
        t = bst.insert(t, 2, 'two')
        self.assertEqual(bst.tree_height(t), 1)
        # self.assertEqual(bst.find_max(t), (2, 'two'))
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        self.assertEqual(bst.tree_height(t), 2)
        t = bst.insert(t, 0, 'zero')
        self.assertEqual(bst.tree_height(t), 3)
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        self.assertEqual(bst.tree_height(t), 5)

    def test_bst_range_search(self):
        t = None
        min = 1
        max = 7
        # Empty tree
        self.assertEqual(bst.range_search(t, min, max), None)
        # 1 Node
        t = bst.insert(t, 4, 'four')
        self.assertEqual(bst.range_search(t, min, max), ['four'])
        t = bst.insert(t, 2, 'two')
        self.assertEqual(bst.range_search(t, min, max), ['two', 'four'])
        # self.assertEqual(bst.find_max(t), (2, 'two'))
        t = bst.insert(t, 5, 'five')
        t = bst.insert(t, 1, 'one')
        t = bst.insert(t, 0, 'zero')
        self.assertEqual(bst.range_search(t, min, max),\
        ['one', 'two', 'four', 'five'])
        t = bst.insert(t, 3, 'three')
        t = bst.insert(t, 9, 'nine')
        t = bst.insert(t, 6, 'six')
        t = bst.insert(t, 7, 'seven')
        t = bst.insert(t, 8, 'eight')
        self.assertEqual(bst.range_search(t, min, max),\
        ['one', 'two', 'three', 'four', 'five', 'six'])

    def test_bst_delete(self):
        t = None
        dummy_node = None #used to compare against bst 't'
        dummy_node = bst.insert(dummy_node, 2, 'two')

        # Empty tree
        self.assertRaises(KeyError, bst.delete, t, 5)

        # Deleting root
        t = bst.insert(t, 4, 'four')
        t = bst.delete(t, 4)  # saves the delete
        self.assertEqual(t, None)

        # Deleting root single child
        t = bst.insert(t, 2, 'two')
        t = bst.insert(t, 5, 'five')
        self.assertEqual(bst.delete(t, 5), dummy_node)

        # Checking KeyError for non-empty tree
        self.assertRaises(KeyError, bst.delete, t, 99)

        t2 = None
        t2 = bst.insert(t2, 4, 'four')
        t2 = bst.insert(t2, 2, 'two')
        t2 = bst.insert(t2, 5, 'five')
        t2 = bst.insert(t2, 1, 'one')
        t2 = bst.insert(t2, 0, 'zero')
        t2 = bst.insert(t2, 3, 'three')
        t2 = bst.insert(t2, 9, 'nine')
        t2 = bst.insert(t2, 6, 'six')
        t2 = bst.insert(t2, 7, 'seven')
        t2 = bst.insert(t2, 8, 'eight')
        t_list = bst.inorder_list(t2)
        # print(t_list)

        t2 = bst.delete(t2, 1)
        t2 = bst.delete(t2, 2)
        t2 = bst.delete(t2, 3)
        t2 = bst.delete(t2, 4)
        t2 = bst.delete(t2, 5)
        t_list = bst.inorder_list(t2)
        self.assertEqual(t_list, [0, 6, 7, 8, 9])
        t2 = bst.delete(t2, 6)
        t2 = bst.delete(t2, 7)
        t2 = bst.delete(t2, 8)
        t2 = bst.delete(t2, 9)
        t2 = bst.delete(t2, 0)
        t_list = bst.inorder_list(t2)
        self.assertEqual(t_list, None)

    def test_classmates(self):
        # substitute the file name and the path with yours.
        filename = '2202-cpe202-05.tsv'
        t = import_classmates(filename)
        self.assertEqual(t.size(), 38)
        # self.assertEqual(t.size(), 55)
        v = search_classmate(t, 14)
        self.assertEqual(v.major, 'EE')
        self.assertEqual(v.last, 'Hua')
        self.assertEqual(v.first, 'Richard')
        self.assertEqual(v.year, 'Senior')
        self.assertRaises(KeyError, search_classmate, t, 0)



if __name__ == '__main__':
    unittest.main()
