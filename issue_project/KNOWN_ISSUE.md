# Known Issue: LR Rotation Bug in AVL Tree

## Issue Type
**Logic Error** - Incorrect operation sequence in Left-Right (LR) rotation

## Summary
The AVL tree implementation contains a deliberate bug in the Left-Right (LR) rotation case. The rotation operations are performed in the wrong order, causing tree structure corruption and loss of balance property.

## Location
- **File**: `src/avl_tree.py`
- **Class**: `AVLTree`
- **Method**: `_insert_recursive()`
- **Lines**: 128-132 (LR rotation case)

## Problem Description

### Expected Behavior
When an LR-type imbalance is detected (left subtree is heavier, and the imbalance is caused by insertion in the left child's right subtree), the correct fix requires:

1. **First**: Perform left rotation on the left child
2. **Second**: Perform right rotation on the parent node

This is a **double rotation** that must be done in the correct sequence.

### Actual Buggy Behavior
The current implementation performs the rotations in reverse order:

```python
# Left-Right (LR) case - **BUG IS HERE**
if balance > 1 and key > node.left.key:
    # WRONG ORDER: Should do left_rotate on child FIRST, then right_rotate on parent
    node = self.right_rotate(node)  # BUG: This should be done SECOND
    node.left = self.left_rotate(node.left)  # BUG: This should be done FIRST
    return node
```

### Correct Implementation Should Be
```python
# Left-Right (LR) case - CORRECT VERSION
if balance > 1 and key > node.left.key:
    node.left = self.left_rotate(node.left)  # FIRST: rotate child
    return self.right_rotate(node)  # SECOND: rotate parent
```

## Impact

### 1. **Tree Structure Corruption**
- Nodes may end up with incorrect parent-child relationships
- Some nodes may become unreachable from the root

### 2. **Loss of Balance Property**
- The tree no longer maintains the AVL balance property (height difference ≤ 1)
- Tree can degrade toward a linked list structure
- Height becomes uncontrolled

### 3. **Performance Degradation**
- Search operations degrade from O(log n) to potentially O(n)
- Database query performance significantly impacted
- Defeats the purpose of using a balanced tree

### 4. **Data Integrity Risk**
- Nodes may be lost during rotation
- Search operations may fail to find existing keys
- Tree traversal may skip nodes

## Trigger Conditions

The bug is triggered when:

1. Inserting a node that causes the left subtree to become heavier (balance > 1)
2. The new key is greater than the left child's key
3. This creates an LR-type imbalance pattern

### Example Trigger Sequence
```python
tree.insert(10)  # Root
tree.insert(5)   # Left child
tree.insert(7)   # Left child's right child - TRIGGERS LR ROTATION BUG
```

This pattern creates:
```
    10
   /
  5
   \
    7
```

Which should be rotated to:
```
   7
  / \
 5   10
```

But the bug causes incorrect structure.

## Test Cases That Fail

### Test 1: Basic LR Rotation
- **File**: `tests/test_avl_tree.py`
- **Test**: `test_lr_rotation_basic()`
- **Assertion**: Tree should be balanced after LR rotation
- **Result**: ❌ FAILS - Tree becomes unbalanced

### Test 2: LR Rotation with Search
- **File**: `tests/test_avl_tree.py`
- **Test**: `test_lr_rotation_with_search()`
- **Assertion**: All inserted nodes should be searchable
- **Result**: ❌ MAY FAIL - Some nodes become unreachable

### Test 3: Complex LR Sequence
- **File**: `tests/test_avl_tree.py`
- **Test**: `test_lr_rotation_complex_sequence()`
- **Assertion**: Tree remains balanced with multiple insertions
- **Result**: ❌ FAILS - Tree loses balance property

### Test 4: Performance Test
- **File**: `tests/test_avl_tree.py`
- **Test**: `test_lr_rotation_performance()`
- **Assertion**: Tree height should remain logarithmic
- **Result**: ❌ FAILS - Height exceeds expected maximum

### Test 5: Database Integration
- **File**: `tests/test_user_database.py`
- **Test**: `test_user_database_lr_scenario()`
- **Assertion**: Database index should remain balanced
- **Result**: ❌ FAILS - Index becomes unbalanced

## How to Reproduce

Run the test suite:
```bash
python -m pytest tests/test_avl_tree.py::TestAVLTreeLRRotation::test_lr_rotation_basic -v
```

Or run all tests:
```bash
python -m unittest discover tests
```

## Fix Strategy (Overview - No Implementation)

The fix requires:

1. **Identify the LR rotation case** in `_insert_recursive()` method
2. **Swap the order of operations**:
   - First: `node.left = self.left_rotate(node.left)`
   - Second: `return self.right_rotate(node)`
3. **Verify all tests pass** after the fix
4. **Validate** that other rotation types (LL, RR, RL) still work correctly

## Additional Notes

- The LL, RR, and RL rotation cases are implemented correctly
- Only the LR case has this specific bug
- The bug is intentionally simple to isolate and fix
- All supporting infrastructure (tests, tree traversal, etc.) works correctly

## References

- [AVL Tree Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
- AVL Tree Rotations: The LR case requires double rotation in specific order
