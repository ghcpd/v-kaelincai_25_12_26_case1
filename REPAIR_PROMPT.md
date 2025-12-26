# PROMPT FOR AI MODEL: FIX AVL TREE ROTATION BUG

## Your Task
You are a senior software engineer. You have been given a project with a buggy AVL tree implementation that is causing database index failures. Your task is to:

1. **Analyze the existing project** to understand the bug
2. **Create a fixed version** in a NEW directory (do NOT modify the original)
3. **Ensure all tests pass** in the fixed version
4. **Maintain code quality** and documentation

## Project Context

### Background
This project implements a user database management system using AVL tree indexing for O(log n) performance. The AVL tree maintains balance through four types of rotations: LL, RR, LR, and RL.

### The Problem
There is a bug in the Left-Right (LR) rotation implementation that causes:
- Tree structure corruption
- Loss of balance property
- Performance degradation from O(log n) to O(n)
- Potential data loss during rotations

### Current Project Structure
```
./
├── src/
│   ├── __init__.py
│   ├── avl_tree.py          # Contains the bug in LR rotation
│   └── user_database.py     # Database implementation using AVL tree
├── tests/
│   ├── __init__.py
│   ├── test_avl_tree.py     # Unit tests - currently FAILING
│   └── test_user_database.py # Integration tests - currently FAILING
├── README.md
├── requirements.txt
└── KNOWN_ISSUE.md           # Detailed bug description
```

## Your Instructions

### Step 1: Read and Understand
Read these files to understand the bug:
1. `KNOWN_ISSUE.md` - Complete bug description
2. `src/avl_tree.py` - The buggy implementation
3. `tests/test_avl_tree.py` - Failing tests

Focus on:
- The `_insert_recursive()` method in `avl_tree.py`
- Lines 128-132 (the LR rotation case)
- Understanding why the rotation order is wrong

### Step 2: Create Fixed Version
Create a NEW directory structure for the fixed version:

```
├── src/
│   ├── __init__.py
│   ├── avl_tree.py          # FIXED VERSION
│   └── user_database.py     # Copy from original (no changes needed)
├── tests/
│   ├── __init__.py
│   ├── test_avl_tree.py     # Copy from original
│   └── test_user_database.py # Copy from original
├── README.md                # Updated to indicate this is the fixed version
├── requirements.txt         # Same as original
└── FIX_SUMMARY.md          # NEW FILE: Document your fix
```

### Step 3: Fix the Bug

In the new `../src/avl_tree.py`:

1. **Locate the buggy LR rotation code** (around lines 128-132)
2. **Fix the rotation order** in the LR case
3. **Add comments** explaining the correct implementation
4. **Ensure no other code is changed** unless absolutely necessary

The bug is specifically in this section:
```python
# Left-Right (LR) case - **BUG IS HERE**
if balance > 1 and key > node.left.key:
    # Current wrong implementation
    node = self.right_rotate(node)
    node.left = self.left_rotate(node.left)
    return node
```

You need to determine and implement the correct rotation sequence.

### Step 4: Create FIX_SUMMARY.md

Create `../FIX_SUMMARY.md` with:

```markdown
# Fix Summary: AVL Tree LR Rotation Bug

## Problem Identified
[Describe what was wrong with the original implementation]

## Root Cause
[Explain why the wrong rotation order caused the bug]

## Solution Implemented
[Describe the fix - what changed and why]

## Code Changes
**File**: src/avl_tree.py
**Method**: _insert_recursive()
**Lines Changed**: [specify line numbers]

### Before (Buggy):
```python
[paste buggy code]
```

### After (Fixed):
```python
[paste fixed code]
```

## Verification
[Explain how you verified the fix works]

- Test results before fix: [list failing tests]
- Test results after fix: [list passing tests]

## Technical Explanation
[Explain the correct LR rotation algorithm and why this order is necessary]
```

### Step 5: Update README

Update `../issue_project_fixed/README.md`:
- Change title to indicate this is the FIXED version
- Remove or update the "Known Issues" section
- Add a section mentioning this is the corrected version

### Step 6: Verify All Tests Pass

Run the tests in the fixed version:
```bash
cd ../issue_project_fixed
python -m pytest tests/ -v
```

OR:
```bash
cd ../issue_project_fixed
python -m unittest discover tests
```

**All tests must pass** for the fix to be considered complete.

## Requirements and Constraints

### Must Do:
✅ Create the fixed project in NEW directory
✅ Fix ONLY the LR rotation bug - do not modify other rotation types
✅ Ensure ALL tests pass after the fix
✅ Create comprehensive FIX_SUMMARY.md documenting your changes
✅ Add clear comments in the fixed code explaining the correct rotation order
✅ Preserve all original test files (just copy them to the new directory)

### Must NOT Do:
❌ Do NOT modify the original project directory
❌ Do NOT change the test files (they are correct)
❌ Do NOT modify the LL, RR, or RL rotation implementations (they are correct)
❌ Do NOT add new dependencies or change the project structure significantly

### Code Quality:
- Maintain the same code style as the original
- Keep comments clear and concise
- Ensure proper indentation and formatting
- Follow Python best practices

## Success Criteria

Your fix will be considered successful when:

1. ✅ New directory issue_project_fixed is created
2. ✅ The LR rotation bug is fixed with correct operation order
3. ✅ ALL unit tests pass (0 failures)
4. ✅ ALL integration tests pass (0 failures)
5. ✅ Tree remains balanced after LR rotations
6. ✅ Search operations work correctly after rotations
7. ✅ Tree height remains logarithmic (O(log n))
8. ✅ FIX_SUMMARY.md clearly documents the fix
9. ✅ Code includes helpful comments explaining the fix

## Expected Test Results

After your fix, running tests should show:

```
test_lr_rotation_basic ... ok
test_lr_rotation_with_search ... ok
test_lr_rotation_complex_sequence ... ok
test_lr_rotation_performance ... ok
test_ll_rotation ... ok
test_rr_rotation ... ok
test_rl_rotation ... ok
test_user_database_lr_scenario ... ok
test_bulk_user_insertion ... ok

----------------------------------------------------------------------
Ran 9 tests in X.XXXs

OK
```

## Hints

<details>
<summary>Click for hints if you're stuck</summary>

### Hint 1: Rotation Order
In LR rotation, think about the visual structure transformation:
- You have a "zig-zag" pattern that needs to become balanced
- Which node should become the new root?
- Work from inner to outer

### Hint 2: The Two Steps
LR rotation is called a "double rotation" for a reason:
- Step 1 straightens the zig-zag into a straight line
- Step 2 balances the straight line

### Hint 3: Compare with RL
The RL (Right-Left) case in the code is implemented correctly.
Look at how it's done and apply the symmetric logic to LR.

</details>

## Questions to Guide Your Analysis

Before implementing the fix, answer these:

1. What is the current rotation order in the buggy code?
2. Why does this order cause the tree structure to break?
3. What should the correct rotation order be?
4. How does this compare to the RL rotation case?
5. What is the visual transformation that should occur?

## Deliverables

When you complete this task, you should have:

1. **Fixed codebase** in issue_project_fixed
2. **FIX_SUMMARY.md** documenting the fix
3. **Updated README.md** indicating this is the fixed version
4. **Test results** showing all tests passing
5. **Clear code comments** explaining the correct rotation

## Start Here

Begin by:
1. Reading `KNOWN_ISSUE.md` thoroughly
2. Examining the buggy code in `src/avl_tree.py`
3. Understanding why the current implementation fails
4. Planning your fix before implementing
5. Creating the new directory structure
6. Implementing and testing the fix

Good luck! This is a focused bug fix task - the fix itself is simple, but understanding WHY it works is the key.
