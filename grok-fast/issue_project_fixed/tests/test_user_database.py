"""
Integration tests for User Database system.
Tests the AVL tree indexing in a realistic database scenario.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.user_database import UserDatabase


class TestUserDatabaseIntegration(unittest.TestCase):
    """Integration tests for user database with AVL indexing."""
    
    def test_user_database_lr_scenario(self):
        """
        Test user database with insertion pattern that triggers LR rotation.
        
        This simulates a real-world scenario where user IDs are added
        in an order that exposes the LR rotation bug.
        """
        db = UserDatabase()
        
        # Simulate adding users with IDs that trigger LR rotation
        users = [
            (1000, {"name": "John Doe", "email": "john@example.com"}),
            (500, {"name": "Jane Smith", "email": "jane@example.com"}),
            (750, {"name": "Bob Johnson", "email": "bob@example.com"}),
        ]
        
        for user_id, user_info in users:
            db.add_user(user_id, user_info)
        
        # Verify all users can be retrieved
        for user_id, expected_info in users:
            retrieved = db.get_user(user_id)
            self.assertIsNotNone(retrieved, 
                               f"Should be able to retrieve user {user_id}")
            self.assertEqual(retrieved["name"], expected_info["name"])
        
        # Verify index is balanced
        self.assertTrue(db.is_index_balanced(),
                       "Database index should remain balanced")
    
    def test_bulk_user_insertion(self):
        """
        Test inserting multiple users and verify index performance.
        
        The LR rotation bug can cause the index to degrade,
        increasing query time from O(log n) to O(n).
        """
        db = UserDatabase()
        
        # Insert users with IDs designed to trigger LR rotations
        user_ids = [100, 50, 75, 25, 60, 55, 150, 125, 140]
        
        for uid in user_ids:
            db.add_user(uid, {
                "name": f"User{uid}",
                "email": f"user{uid}@example.com",
                "department": "Engineering"
            })
        
        # Verify all users are retrievable
        for uid in user_ids:
            user = db.get_user(uid)
            self.assertIsNotNone(user, f"User {uid} should be retrievable")
            self.assertEqual(user["name"], f"User{uid}")
        
        # Verify IDs are returned in sorted order
        all_ids = db.get_all_user_ids()
        self.assertEqual(all_ids, sorted(user_ids))
        
        # Verify index height is logarithmic (not linear)
        # For 9 nodes, height should be at most 4
        height = db.get_index_height()
        self.assertLessEqual(height, 4,
                            f"Index height {height} suggests unbalanced tree")


if __name__ == '__main__':
    unittest.main()