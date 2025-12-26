# Fix Summary: AVL Tree LR Rotation Bug

## Problem Identified
The original `AVLTree._insert_recursive()` implemented the Left-Right (LR)
rotation in the wrong order, which produced corrupted tree structure and
violated the AVL balance invariants when an LR case was triggered.

## Root Cause
The LR case is a double rotation that must first rotate the *child* (left
child) left, then rotate the *parent* right. The buggy code performed the
parent rotation first and then rotated the (now-misplaced) child — this
reordered links incorrectly and produced unreachable nodes.

## Solution Implemented
- Fixed the LR rotation sequence to perform `node.left = left_rotate(node.left)`
  **first**, then `return right_rotate(node)`.
- Added clarifying comments in `src/avl_tree.py` explaining why the order
  matters.
- Did not change LL, RR, or RL logic; tests and public API remain unchanged.

## Code Changes
**File**: `src/avl_tree.py`  
**Method**: `_insert_recursive()`  
**Lines Changed**: original implementation around lines **128-132** (LR case)

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
    # 1) Left-rotate the left child to straighten the zig-zag
    node.left = self.left_rotate(node.left)
    # 2) Right-rotate the current node to balance the subtree
    return self.right_rotate(node)
```

## Technical Explanation
LR is a "zig-zag" pattern (parent -> left -> right). The correct
transformation is:
1. Rotate the inner child to convert zig-zag into a straight line (child
   rotation).
2. Rotate the parent to balance the subtree (parent rotation).

Reversing these steps breaks parent/child links and can leave nodes
unreachable or produce incorrect heights.

## Verification
- Test results before fix: multiple LR-related tests failed (see
  `KNOWN_ISSUE.md`) — `test_lr_rotation_basic`, `test_lr_rotation_with_search`,
  `test_lr_rotation_complex_sequence`, `test_lr_rotation_performance`, and the
  database integration test `test_user_database_lr_scenario`.

- Test results after fix: ALL TESTS PASS

  Command used:
  ```bash
  python -m pytest tests/ -q
  ```

  Output (fixed project):
  ```
  ........                                                                 [100%]
  8 passed in 0.05s
  ```

How I verified:
1. Created a separate fixed copy at `issue_project_fixed/` (original left intact).
2. Applied the LR rotation order fix only in `src/avl_tree.py`.
3. Ran the full test suite (`tests/`) — all unit and integration tests passed.

---

## Notes
- Only the LR case was modified; all other rotation code and tests were kept
  intact to preserve behavior and ensure targeted fixability.
- The fix follows the standard AVL double-rotation algorithm.
