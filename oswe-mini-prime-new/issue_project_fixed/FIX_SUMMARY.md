# Fix Summary: AVL Tree LR Rotation Bug

## Problem Identified
The original AVL tree implementation performed the Left-Right (LR) rotation in the wrong order. The LR case executed a right rotation on the parent first and then a left rotation on the (new) left child — this is reversed and corrupts the tree structure.

## Root Cause
The LR double rotation must first *left-rotate the left child* to convert the zig-zag into a straight line, and *then* right-rotate the parent to balance the subtree. Doing the rotations in the reverse order breaks parent-child links and can make nodes unreachable.

## Solution Implemented
Updated `src/avl_tree.py` in the `_insert_recursive()` method: swapped the rotation order for the LR case and added explanatory comments.

## Code Changes
**File**: `src/avl_tree.py`
**Method**: `_insert_recursive()`
**Lines Changed**: LR rotation case (previously around lines ~128-132 in original file)

### Before (Buggy):
```python
# Left-Right (LR) case - **BUG IS HERE**
if balance > 1 and key > node.left.key:
    # WRONG ORDER: Should do left_rotate on child FIRST, then right_rotate on parent
    node = self.right_rotate(node)  # BUG: This should be done SECOND
    node.left = self.left_rotate(node.left)  # BUG: This should be done FIRST
    return node
```

### After (Fixed):
```python
# Left-Right (LR) case - FIXED
if balance > 1 and key > node.left.key:
    # Correct LR double rotation sequence:
    # 1) First perform LEFT rotation on the left child to "straighten" the zig-zag
    # 2) Then perform RIGHT rotation on the unbalanced node (parent)
    node.left = self.left_rotate(node.left)  # FIRST: rotate child
    return self.right_rotate(node)          # SECOND: rotate parent
```

## Verification
- Test results before fix: Several unit and integration tests failed (LR-related tests).
- Test results after fix: All provided tests pass (unit + integration).

### Tests executed
- `tests/test_avl_tree.py` - all LR tests pass
- `tests/test_user_database.py` - integration tests pass

## Technical Explanation
The LR case arises when a node's left subtree is heavy (balance > 1) and the insertion happens in the left child's right subtree (key > node.left.key). The correct operation is a double rotation that first rotates the left child left (to convert the LR case to LL), then rotates the parent right to rebalance the subtree. This order preserves parent/child link invariants and ensures the correct subtree root after rotations.

## Notes
- LL, RR, and RL implementations were not modified (they were correct).
- The fix preserves the original code style and includes comments that explain the rotation order.
