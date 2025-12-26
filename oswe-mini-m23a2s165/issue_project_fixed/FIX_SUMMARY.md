# Fix Summary: AVL Tree LR Rotation Bug

## Problem Identified
The original `AVLTree._insert_recursive()` implemented the Left-Right (LR)
case using the wrong rotation order. The code performed a right rotation
on the parent before rotating the left child, which corrupted the tree
structure and broke the AVL balance invariants.

## Root Cause
LR is a "double rotation" case that requires first rotating the **left
child** to straighten the zig-zag, then rotating the **parent** to
rebalance. Reversing that order leaves child/parent pointers in an
invalid configuration and can make nodes unreachable from the root.

## Solution Implemented
- Fixed the LR case in `src/avl_tree.py` so that it performs
  `node.left = left_rotate(node.left)` first, followed by
  `return right_rotate(node)`.
- Added explanatory comments in the code to make the correct order
  explicit.

## Code Changes
**File**: `src/avl_tree.py`  
**Method**: `_insert_recursive()`  
**Lines Changed**: LR rotation block (small localized change)

### Before (Buggy):
```python
# Left-Right (LR) case - **BUG IS HERE**
if balance > 1 and key > node.left.key:
    # WRONG ORDER: Should do left_rotate on child FIRST, then right_rotate on parent
    # Current buggy implementation does it backwards
    node = self.right_rotate(node)  # BUG: This should be done SECOND
    node.left = self.left_rotate(node.left)  # BUG: This should be done FIRST
    return node
```

### After (Fixed):
```python
# Left-Right (LR) case - FIXED
if balance > 1 and key > node.left.key:
    # Correct LR double-rotation order:
    # 1) Rotate left on the left child to convert LR into LL
    # 2) Rotate right on the parent node to balance
    node.left = self.left_rotate(node.left)  # FIRST: fix child
    return self.right_rotate(node)           # SECOND: fix parent
```

## Verification
- Test results before fix: several tests in `tests/test_avl_tree.py` and
  `tests/test_user_database.py` that exercise LR scenarios were failing
  (see `KNOWN_ISSUE.md` for details).
- Test results after fix: all provided unit and integration tests pass.

## Technical Explanation
Visually, LR imbalance looks like:

    z                z                y
   /                /                / \
  x      ->       y      ->        x   z
   \              /                
    y            x

To correct it:
1. Left-rotate the left child (`x`) so the zig-zag becomes a straight
   left-left case.
2. Right-rotate the parent (`z`) to finish rebalancing.

Doing the steps in the opposite order breaks parent/child links and
produces an invalid tree.

## Files Added / Modified
- Modified: `src/avl_tree.py` (fixed LR order, added comments)
- Added: `FIX_SUMMARY.md`
- Copied: other source & test files into `issue_project_fixed/` (no changes)

## Conclusion
The LR rotation bug was a small but critical logic error. The fix is
localized, well-documented, and verified by the existing test suite.
All tests pass after the change.
