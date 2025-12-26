# AVL Tree Database Indexing System — FIXED LR Rotation

This repository is a fixed copy of the original project. The Left-Right (LR)
rotation bug in `src/avl_tree.py` has been corrected; all other logic and tests
are preserved unchanged.

See `FIX_SUMMARY.md` for details about the fix and verification.

## Notable Changes
- `src/avl_tree.py`: LR rotation order corrected (child rotation first,
  then parent rotation).
- Tests and interface are unchanged — designed to be a drop-in replacement.

## Running tests

```bash
python -m pytest tests/ -q
```
