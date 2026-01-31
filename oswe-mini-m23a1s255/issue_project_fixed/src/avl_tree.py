"""
AVL Tree Implementation for Database Indexing — FIXED LR rotation

This is a fixed copy of the original `avl_tree.py` with the LR (Left-Right)
rotation order corrected. The rest of the implementation is preserved to
remain compatible with the existing tests.
"""


class Node:
    """Represents a node in the AVL tree."""
    
    def __init__(self, key, user_data=None):
        self.key = key
        self.user_data = user_data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL Tree implementation for database indexing.
    Maintains O(log n) performance for insert, delete, and search operations.
    """
    
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        """Returns the height of a node."""
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        """Returns the balance factor of a node."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        """Updates the height of a node based on its children."""
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))
    
    def right_rotate(self, z):
        """
        Performs right rotation on node z.
        """
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        self.update_height(z)
        self.update_height(y)
        
        return y
    
    def left_rotate(self, z):
        """
        Performs left rotation on node z.
        """
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        self.update_height(z)
        self.update_height(y)
        
        return y
    
    def insert(self, key, user_data=None):
        """Inserts a new key-value pair into the AVL tree."""
        self.root = self._insert_recursive(self.root, key, user_data)
    
    def _insert_recursive(self, node, key, user_data):
        """Helper method for recursive insertion with balancing."""
        # Step 1: Perform normal BST insertion
        if not node:
            return Node(key, user_data)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, user_data)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, user_data)
        else:
            # Duplicate keys not allowed
            return node
        
        # Step 2: Update height of current node
        self.update_height(node)
        
        # Step 3: Get balance factor
        balance = self.get_balance(node)
        
        # Step 4: If unbalanced, handle 4 cases
        
        # Left-Left (LL) case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        
        # Right-Right (RR) case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        
        # Left-Right (LR) case - FIXED
        if balance > 1 and key > node.left.key:
            # Correct LR (double) rotation order:
            # 1) Left-rotate the left child to straighten the zig-zag
            # 2) Right-rotate the current node to balance the subtree
            #
            # This must be done in this order (child first, then parent).
            node.left = self.left_rotate(node.left)  # STEP 1
            return self.right_rotate(node)           # STEP 2
        
        # Right-Left (RL) case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def search(self, key):
        """Searches for a key in the tree and returns the associated user data."""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """Helper method for recursive search."""
        if not node:
            return None
        
        if key == node.key:
            return node.user_data
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def inorder_traversal(self):
        """Returns a list of keys in sorted order."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def get_tree_height(self):
        """Returns the height of the entire tree."""
        return self.get_height(self.root)
    
    def is_balanced(self):
        """Checks if the tree is balanced (for debugging purposes)."""
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        """Helper method to check if tree is balanced."""
        if not node:
            return True
        
        balance = self.get_balance(node)
        if abs(balance) > 1:
            return False
        
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))
