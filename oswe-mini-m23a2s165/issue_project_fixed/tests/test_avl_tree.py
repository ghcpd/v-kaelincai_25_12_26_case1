"""
Unit tests for AVL Tree implementation.
These tests reveal the LR rotation bug in the AVL tree.
"""

import unittest
import sys
import os

# Add parent directory to path to import src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.avl_tree import AVLTree


class TestAVLTreeLRRotation(unittest.TestCase):
    """Test cases specifically for Left-Right rotation scenario."""
    
    def test_lr_rotation_basic(self):
        tree = AVLTree()
        tree.insert(10, {"name": "User10"})
        tree.insert(5, {"name": "User5"})
        tree.insert(7, {"name": "User7"})
        self.assertTrue(tree.is_balanced(), "Tree should be balanced after LR rotation")
        self.assertEqual(tree.root.key, 7, "Root should be 7 after LR rotation")
        self.assertEqual(tree.get_tree_height(), 2, "Tree height should be 2 for 3 nodes in balanced tree")
    
    def test_lr_rotation_with_search(self):
        tree = AVLTree()
        tree.insert(20, {"name": "Alice", "dept": "Engineering"})
        tree.insert(10, {"name": "Bob", "dept": "Sales"})
        tree.insert(15, {"name": "Charlie", "dept": "Marketing"})
        self.assertIsNotNone(tree.search(20), "Should find key 20")
        self.assertIsNotNone(tree.search(10), "Should find key 10")
        self.assertIsNotNone(tree.search(15), "Should find key 15")
        self.assertEqual(tree.search(15)["name"], "Charlie")
    
    def test_lr_rotation_complex_sequence(self):
        tree = AVLTree()
        keys = [50, 25, 75, 10, 30, 27]
        for key in keys:
            tree.insert(key, {"id": key})
        self.assertTrue(tree.is_balanced(), "Tree should remain balanced after complex insertions")
        for key in keys:
            self.assertIsNotNone(tree.search(key), f"Should be able to find key {key}")
        result = tree.inorder_traversal()
        self.assertEqual(result, sorted(keys), "Inorder traversal should return sorted keys")
    
    def test_lr_rotation_performance(self):
        tree = AVLTree()
        insertion_patterns = [
            (100, 50, 75),
            (200, 150, 175),
            (300, 250, 275)
        ]
        for root, left, middle in insertion_patterns:
            tree.insert(root)
            tree.insert(left)
            tree.insert(middle)
        actual_height = tree.get_tree_height()
        self.assertLessEqual(actual_height, 4, f"Tree height {actual_height} exceeds expected maximum for balanced tree with 9 nodes")


class TestAVLTreeOtherRotations(unittest.TestCase):
    def test_ll_rotation(self):
        tree = AVLTree()
        tree.insert(30)
        tree.insert(20)
        tree.insert(10)
        self.assertTrue(tree.is_balanced())
        self.assertEqual(tree.root.key, 20)
    
    def test_rr_rotation(self):
        tree = AVLTree()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)
        self.assertTrue(tree.is_balanced())
        self.assertEqual(tree.root.key, 20)
    
    def test_rl_rotation(self):
        tree = AVLTree()
        tree.insert(10)
        tree.insert(30)
        tree.insert(20)
        self.assertTrue(tree.is_balanced())
        self.assertEqual(tree.root.key, 20)


if __name__ == '__main__':
    unittest.main()
