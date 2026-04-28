# Patterns Index

Master table of contents for all DSA patterns. Use this to navigate the pattern guides and understand which technique to apply for a given problem.

## All Patterns

| Pattern | Problems | Difficulty Range | Best For |
|---------|----------|------------------|----------|
| [Hashing](hashing.md) | 9 | Easy–Hard | Duplicate detection, index-as-hash |
| [Sliding Window](sliding-window.md) | 3 | Medium–Hard | Subarray/substring optimization |

---

## Pattern Selection Guide

**Finding the right pattern for a problem:**

- **"Find two elements that..."** → Hashing or Two Pointers
- **"Find a contiguous subarray/substring..."** → Sliding Window or Two Pointers
- **"Optimal value (max, min, count)..."** → Dynamic Programming or Greedy
- **"Duplicates, anagrams, grouping..."** → Hashing
- **"Converging from ends, pairs..."** → Two Pointers

---

## Quick Links

- [All Problems](../problems/) — individual problem notes
- [Sessions](../sessions/) — daily work logs
- [db.json](../db.json) — problem metadata

## Query Problems by Pattern

```bash
# List all problems using hashing
python3 scripts/query.py pattern hashing

# List all unsolved problems
python3 scripts/query.py unsolved

# Show follow-ups for a problem
python3 scripts/query.py followups 0217
```
