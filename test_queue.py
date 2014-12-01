#!/usr/bin/env python

import unittest
from Queue import Queue

class TestQueueADT(unittest.TestCase):

  def setUp(self):
    self.my_queue = Queue()

  def test_exceptions(self): 
    self.assertRaises(IndexError, self.my_queue.dequeue)

  def test_queue_operations(self):
    self.assertEquals(self.my_queue.is_empty(), True)
    queue_elements = ["First", "Second", "Third", "Fourth"]
    counter = 0
    while counter < len(queue_elements):
      self.my_queue.enqueue(queue_elements[counter])
      self.assertEquals(self.my_queue.is_empty(), False)
      counter += 1

    counter = 0
    while counter < len(queue_elements):
      self.assertEquals(self.my_queue.dequeue(), queue_elements[counter])
      counter += 1
   
    self.assertEquals(self.my_queue.is_empty(), True) 
    

if __name__ == '__main__':
  unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)

