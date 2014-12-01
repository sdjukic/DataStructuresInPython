#!/usr/bin/env python

import unittest
from BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

  def setUp(self):
    self.my_bst = BinarySearchTree()
    self.tree_values = [25, 50, 12, 35, 5, 60, 17, 1]
    for value in self.tree_values:
      self.my_bst.insert(value)

  def test_exceptions(self): 
    self.assertRaises(AttributeError, self.my_bst.insert, 50)
    self.assertRaises(AttributeError, self.my_bst.insert, 12)
    self.assertRaises(AttributeError, self.my_bst.insert, 35)
    self.assertRaises(AttributeError, self.my_bst.insert, 1)

  def test_tree_operations(self):

    self.assertEquals(self.my_bst.find(13), False)
    self.assertEquals(self.my_bst.find(27), False)

    for val in self.tree_values:
      self.assertTrue(self.my_bst.find(val))
   
    
    self.assertIsNone(self.my_bst.delete(12))

if __name__ == '__main__':
  unittest.main()

