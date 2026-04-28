# Hashing

A pattern for using hash maps/sets to achieve O(1) lookups and aggregation.

## Key Insights
- Trade space for time: store seen elements in a hash map to avoid repeated searching
- Useful for finding pairs, grouping, counting, or detecting duplicates
- Watch out for: hash collisions (rare in practice), memory usage on large datasets

## Pattern Evolution Chain

The hashing pattern progresses through duplicate detection and variant handling:

**Tier 1 (Duplicate detection):**
→ [0217 - Contains Duplicate](../problems/0217-contains-duplicate.md) ➜ [0442 - Find All Duplicates in an Array](../problems/0442-find-all-duplicates-in-array.md)

## Problems

| # | Name | Difficulty | Status | Notes |
|---|------|-----------|--------|-------|
| 0217 | [Contains Duplicate](../problems/0217-contains-duplicate.md) | Easy | ✅ | Set tracking, foundational |
| 0219 | [Contains Duplicate II](../problems/0219-contains-duplicate-ii.md) | Easy | ⏳ | Index constraint, sliding window |
| 0220 | [Contains Duplicate III](../problems/0220-contains-duplicate-iii.md) | Hard | ⏳ | Value + index constraints |
| 0442 | [Find All Duplicates in an Array](../problems/0442-find-all-duplicates-in-an-array.md) | Medium | ✅ | In-place marking, [1,n] constraint |
| 0448 | [Find All Numbers Disappeared in an Array](../problems/0448-find-all-numbers-disappeared.md) | Easy | ⏳ | Missing numbers via sign-marking |
| 0041 | [First Missing Positive](../problems/0041-first-missing-positive.md) | Hard | ⏳ | Placement + marking, harder variant |

## Template for New Problem

When adding a hashing problem:
1. Use a hash map to store: `{value: index}`, `{value: count}`, or `{canonical_form: items}`
2. Iterate once or twice through the input
3. Return the result in O(n) or O(n + k) time

## Related Patterns
- **Counting** (variant): Use dict for frequencies
- **Anagrams** (variant): Sort and use as key
