# AVL Tree Database Indexing System - FIXED VERSION

A user database management system that uses AVL tree for maintaining balanced indexes to ensure O(log n) performance for insert, delete, and search operations.

## Project Overview

This project implements an AVL (Adelson-Velsky and Landis) tree data structure for database indexing. The AVL tree maintains balance through rotations, ensuring optimal query performance.

**This is the corrected version** with the LR rotation bug fixed.

## Features

- **Balanced Tree Structure**: Automatically maintains balance through rotations
- **Fast Operations**: O(log n) time complexity for insert, search, and delete
- **User Database**: Practical implementation for managing user records
- **Comprehensive Testing**: Unit and integration tests included

## Project Structure

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   ├── avl_tree.py          # Core AVL tree implementation (FIXED)
│   └── user_database.py     # User database using AVL indexing
├── tests/
│   ├── __init__.py
│   ├── test_avl_tree.py     # Unit tests for AVL tree
│   └── test_user_database.py # Integration tests for database
├── README.md                # This file
├── requirements.txt
└── FIX_SUMMARY.md          # Documentation of the fix
```

## Installation

1. Ensure you have Python 3.7+ installed
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Execute all tests with:

```bash
python -m pytest tests/ -v
```

Or run tests using unittest:

```bash
python -m unittest discover tests
```

## Usage Example

```python
from src.user_database import UserDatabase

# Create database
db = UserDatabase()

# Add users
db.add_user(1000, {"name": "John Doe", "email": "john@example.com"})
db.add_user(500, {"name": "Jane Smith", "email": "jane@example.com"})
db.add_user(750, {"name": "Bob Johnson", "email": "bob@example.com"})

# Retrieve user
user = db.get_user(750)
print(user)  # {"name": "Bob Johnson", "email": "bob@example.com"}

# Get all user IDs in sorted order
all_ids = db.get_all_user_ids()
print(all_ids)  # [500, 750, 1000]
```

## AVL Tree Rotation Types

The AVL tree handles four imbalance cases:

1. **Left-Left (LL)**: Right rotation
2. **Right-Right (RR)**: Left rotation
3. **Left-Right (LR)**: Left rotation on child, then right rotation on parent
4. **Right-Left (RL)**: Right rotation on child, then left rotation on parent

## Fix Summary

This version contains the fix for the LR rotation bug that was present in the original version. See [FIX_SUMMARY.md](FIX_SUMMARY.md) for detailed information about the bug and the solution.

## Technical Details

- **Language**: Python 3.7+
- **Testing Framework**: unittest / pytest
- **Data Structure**: AVL Tree (self-balancing binary search tree)

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert    | O(log n)       | O(1)            |
| Search    | O(log n)       | O(1)            |
| Delete    | O(log n)       | O(1)            |
| Traversal | O(n)           | O(n)            |

## License

This is a test project for educational purposes.