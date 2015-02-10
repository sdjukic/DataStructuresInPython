#!/usr/bin/env python

import unittest
from LinkedList import LinkedList

class TestLinkedListADT(unittest.TestCase):
  
  def setUp(self):
    self.my_list = LinkedList()
    self.my_list.insert(1, "first")
    self.my_list.insert(2, "second")
    self.my_list.insert(3, "third")
    self.my_list.insert(4, "fourth")
    self.my_list.insert(5, "fifth")

  
  def test_exceptions(self):
    self.assertRaises(AttributeError, self.my_list.insert(12, "error"))
    self.assertRaises(AttributeError, self.my_list._remove(10, "error"))

  def test_list_behavior(self):
    self.assertEqual(self.my_list._retrieve_value(1), "first")
    self.assertEqual(self.my_list.size, 5)
    self.my_list._swap(2,4)
    self.assertEqual(self.my_list._retrieve_value(4), "second")
    self.assertEqual(self.my_list._retrieve_value(2), "fourth")



if __name__ == '__main__':
  unittest.main()
