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
        """
        Test basic LR rotation case.
        
        This test inserts nodes in a pattern that triggers LR rotation:
        - Insert 10 (root)
        - Insert 5 (left child - creates imbalance opportunity)
        - Insert 7 (left child's right child - triggers LR case)
        
        Expected tree structure after proper LR rotation:
              7
             / \
            5   10
            
        Current buggy implementation will create an incorrect structure.
        """
        tree = AVLTree()
        
        # Insert sequence that triggers LR rotation
        tree.insert(10, {"name": "User10"})
        tree.insert(5, {"name": "User5"})
        tree.insert(7, {"name": "User7"})  # This triggers LR rotation
        
        # After proper LR rotation, tree should be balanced
        self.assertTrue(tree.is_balanced(), 
                       "Tree should be balanced after LR rotation")
        
        # Root should be 7 after proper rotation
        self.assertEqual(tree.root.key, 7, 
                        "Root should be 7 after LR rotation")
        
        # Height should be minimal (2) for 3 nodes
        self.assertEqual(tree.get_tree_height(), 2,
                        "Tree height should be 2 for 3 nodes in balanced tree")
    
    def test_lr_rotation_with_search(self):
        """
        Test that search works correctly after LR rotation.
        
        The bug in LR rotation can cause nodes to become unreachable,
        leading to search failures.
        """
        tree = AVLTree()
        
        # Insert sequence triggering LR rotation
        tree.insert(20, {"name": "Alice", "dept": "Engineering"})
        tree.insert(10, {"name": "Bob", "dept": "Sales"})
        tree.insert(15, {"name": "Charlie", "dept": "Marketing"})
        
        # All nodes should be searchable
        self.assertIsNotNone(tree.search(20), "Should find key 20")
        self.assertIsNotNone(tree.search(10), "Should find key 10")
        self.assertIsNotNone(tree.search(15), "Should find key 15")
        
        # Verify correct data is returned
        self.assertEqual(tree.search(15)["name"], "Charlie")
    
    def test_lr_rotation_complex_sequence(self):
        """
        Test LR rotation with a more complex insertion sequence.
        
        This test inserts multiple nodes that trigger LR rotation
        and verifies the tree maintains balance and correct ordering.
        """
        tree = AVLTree()
        
        # Sequence that triggers LR rotation multiple times
        keys = [50, 25, 75, 10, 30, 27]
        
        for key in keys:
            tree.insert(key, {"id": key})
        
        # Tree should remain balanced
        self.assertTrue(tree.is_balanced(),
                       "Tree should remain balanced after complex insertions")
        
        # All keys should be searchable
        for key in keys:
            self.assertIsNotNone(tree.search(key),
                               f"Should be able to find key {key}")
        
        # Inorder traversal should return sorted keys
        result = tree.inorder_traversal()
        self.assertEqual(result, sorted(keys),
                        "Inorder traversal should return sorted keys")
    
    def test_lr_rotation_performance(self):
        """
        Test that tree height remains logarithmic after LR rotations.
        
        The bug causes the tree to become unbalanced, degrading from
        O(log n) to O(n) performance.
        """
        tree = AVLTree()
        
        # Insert pattern that repeatedly triggers LR rotation
        # Pattern: insert root, left child, then middle value
        insertion_patterns = [
            (100, 50, 75),
            (200, 150, 175),
            (300, 250, 275)
        ]
        
        for root, left, middle in insertion_patterns:
            tree.insert(root)
            tree.insert(left)
            tree.insert(middle)
        
        # For 9 nodes, height should not exceed 4 in a balanced tree
        # (log2(9) ≈ 3.17, so height of 4 is acceptable)
        actual_height = tree.get_tree_height()
        self.assertLessEqual(actual_height, 4,
                            f"Tree height {actual_height} exceeds expected maximum "
                            f"for balanced tree with 9 nodes")


class TestAVLTreeOtherRotations(unittest.TestCase):
    """Test cases for other rotation types (LL, RR, RL) to ensure they work."""
    
    def test_ll_rotation(self):
        """Test Left-Left rotation works correctly."""
        tree = AVLTree()
        
        # LL case: insert 30, 20, 10
        tree.insert(30)
        tree.insert(20)
        tree.insert(10)
        
        self.assertTrue(tree.is_balanced())
        self.assertEqual(tree.root.key, 20)
    
    def test_rr_rotation(self):
        """Test Right-Right rotation works correctly."""
        tree = AVLTree()
        
        # RR case: insert 10, 20, 30
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)
        
        self.assertTrue(tree.is_balanced())
        self.assertEqual(tree.root.key, 20)
    
    def test_rl_rotation(self):
        """Test Right-Left rotation works correctly."""
        tree = AVLTree()
        
        # RL case: insert 10, 30, 20
        tree.insert(10)
        tree.insert(30)
        tree.insert(20)
        
        self.assertTrue(tree.is_balanced())
        self.assertEqual(tree.root.key, 20)


if __name__ == '__main__':
    unittest.main()
