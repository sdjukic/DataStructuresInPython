#!/usr/bin/env python3

# Again from Eric Schles implementation of Binary Search Tree

class Node(object):
    def __init__(self, item, left=None, right=None):
        self.item  = item
        self.left  = left
        self.right = right

    def __str__(self):
        return repr(self.item)

class BST(object):
    def __init__(self, root=None, left=None, right=None):
        self.root = Node(root)
        self.root.left = left
        self.root.right = right

    def insert(self, value):
        if self.root.item == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, curr, value):
        if curr.item > value and curr.left == None:
            node = Node(value)
            curr.left = node
        elif curr.item < value and curr.right == None:
            node = Node(value)
            curr.right = node
        else:  
            if curr.item < value:
                self._insert(curr.right, value)
            else:
                self._insert(curr.left, value)

    def contains(self, value):
        if self.root.item == value:
            return True
        else:
            return self._contains(self.root, value)

    def _contains(self, curr, value):
        if curr.item == value:
            return True
        if value < curr.item:
            if curr.left != None:
                return self._contains(curr.left, value)
            else:
                return False
        elif value > curr.item:
            if curr.right != None:
                return self._contains(curr.right, value)
            else:
                return False
        else:
            return False
    

    def second_highest_node(self,node):
        if node.right != None:
            return self._second_highest_node(node)
        else:
            return None

    def _second_highest_node(self,curr):
        next_node = curr.right
        if next_node.right != None:
            return self._second_highest_node(next_node)
        else:
            return curr

    def highest(self,node):
        return self._highest(node)

    def _highest(self,curr):
        if curr.right != None:
            return self._highest(curr.right)
        else:
            return curr.item

    def second_lowest_node(self,node):
        if node.left != None:
            return self._second_lowest_node(node)
        else:
            return None

    def _second_lowest_node(self,curr):
        next_node = curr.left
        if next_node.left != None:
            return self._second_highest_node(next_node)
        else:
            return curr

    def lowest(self,node):
        return self._lowest(node)

    def _lowest(self,curr):
        if curr.left != None:
            return self._lowest(curr.left)
        else:
            return curr.item

    def delete(self, value):
        return self._delete(self.root, value, None)

    def _delete(self, curr, value, parent):
        if value == curr.item:
            if curr.left != None:
                curr.item = self.highest(curr.left)
                second_largest_node = self.second_highest_node(curr.left)
                if second_largest_node != None:
                    second_largest_node.right = None
                    return value
                else:
                    curr.left = None
                    return value

            elif curr.right != None:
                curr.item = self.lowest(curr.right)
                second_smallest_node = self.second_lowest_node(curr.right)
                if second_smallest_node != None:
                    second_smallest_node.left = None
                    return value
                else:
                    curr.right = None
                    return value
            else:
                if parent.left.item == value:
                    parent.left = None
                    return value
                else:
                    parent.right = None
                    return value
        else:
            if value < curr.item and curr.left != None:
                self._delete(curr.left,value,curr)
            elif value > curr.item and curr.right != None:
                self._delete(curr.right,value,curr)
            else:
                return None

