# AVL Tree Database Indexing System (FIXED)

This repository is the fixed version of the original project where the Left-Right (LR) rotation bug in the AVL tree implementation has been corrected.

## What Changed
- Fixed the LR rotation order in `src/avl_tree.py` (left-rotate the left child, then right-rotate the parent)
- Added `FIX_SUMMARY.md` documenting the problem, cause, and fix

## How to Run Tests
```bash
cd issue_project_fixed
python -m pytest tests/ -v
```

All tests were copied from the original project and should pass after the LR rotation fix.
