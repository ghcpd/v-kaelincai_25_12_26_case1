# AVL Tree Database Indexing System — FIXED LR Rotation

This repository is a corrected version of the original `issue_project`.
The Left-Right (LR) rotation bug in the AVL tree implementation has been fixed.

## What's changed
- Fixed LR double-rotation ordering in `src/avl_tree.py` (child rotation first, then parent).
- All unit and integration tests included with the project now pass.

## How to run tests

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## Notes
- The fix is limited to the LR case; LL, RR, and RL rotations were not modified.
- See `FIX_SUMMARY.md` for a full description of the bug, root cause, and verification.
