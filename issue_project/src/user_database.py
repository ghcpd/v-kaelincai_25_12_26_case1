"""
User Database Management System
Uses AVL tree indexing for fast user record lookups.
"""

from .avl_tree import AVLTree


class UserDatabase:
    """Database for managing user records with AVL tree indexing."""
    
    def __init__(self):
        self.index = AVLTree()
    
    def add_user(self, user_id, user_info):
        """
        Adds a user to the database.
        
        Args:
            user_id: Unique user identifier (integer)
            user_info: Dictionary containing user information
        """
        self.index.insert(user_id, user_info)
    
    def get_user(self, user_id):
        """
        Retrieves user information by ID.
        
        Args:
            user_id: User identifier to search for
            
        Returns:
            User information dictionary or None if not found
        """
        return self.index.search(user_id)
    
    def get_all_user_ids(self):
        """Returns all user IDs in sorted order."""
        return self.index.inorder_traversal()
    
    def get_index_height(self):
        """Returns the height of the index tree (for performance monitoring)."""
        return self.index.get_tree_height()
    
    def is_index_balanced(self):
        """Checks if the index tree is properly balanced."""
        return self.index.is_balanced()
