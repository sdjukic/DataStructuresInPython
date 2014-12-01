#!/usr/bin/env python

import unittest
from Stack import Stack

class TestStackADT(unittest.TestCase):
  
  def setUp(self):
    self.my_stack = Stack()

  def test_exceptions(self): 
    self.assertRaises(IndexError, self.my_stack.pop)
    self.assertRaises(IndexError, self.my_stack.top)

  def test_stack_behavior(self):
    self.my_stack.push(10)
    self.assertEqual(self.my_stack.top(), 10)
    self.my_stack.push(14)
    self.assertEqual(self.my_stack.top(), 14)
    self.my_stack.push(21)
    self.assertEqual(self.my_stack.is_empty(), False)

    stack_elements = [21, 14, 10]
    counter = 0
    while not self.my_stack.is_empty():
      self.assertEqual(self.my_stack.top(), stack_elements[counter])
      self.my_stack.pop()
      counter += 1




if __name__ == '__main__':
  unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)
