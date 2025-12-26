"""Integration tests for UserDatabase using AVL index."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.user_database import UserDatabase


class TestUserDatabaseIntegration(unittest.TestCase):
    def test_user_database_lr_scenario(self):
        db = UserDatabase()

        # Insert sequence that triggers LR rotation in the underlying index
        db.add_user(10, {"name": "User10"})
        db.add_user(5, {"name": "User5"})
        db.add_user(7, {"name": "User7"})

        # Index should be balanced and all users searchable
        self.assertTrue(db.is_index_balanced())
        self.assertIsNotNone(db.get_user(5))
        self.assertIsNotNone(db.get_user(7))
        self.assertIsNotNone(db.get_user(10))
