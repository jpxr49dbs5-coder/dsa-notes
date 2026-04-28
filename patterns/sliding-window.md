# Sliding Window

A pattern for problems involving contiguous subarrays or substrings, optimized with a moving window to avoid recomputation.

## Key Insights
- Use two pointers (left and right) to maintain a window
- Expand right pointer to grow window, shrink left to shrink
- Track window state (sum, count, frequency) efficiently
- Useful for: subarray sums, longest substrings, minimum windows

## Pattern Evolution Chain

The sliding window pattern progresses through fixed-size windows to variable-size:

**Tier 1 (Fixed size windows):**
→ [0567 - Permutation in String](../problems/0567-permutation-in-string.md) ➜ [0438 - Find All Anagrams in a String](../problems/0438-find-all-anagrams-in-a-string.md)

**Tier 2 (Variable size windows):**
→ [0076 - Minimum Window Substring](../problems/0076-minimum-window-substring.md)

## Problems

| # | Name | Difficulty | Status | Notes |
|---|------|-----------|--------|-------|
| 0567 | [Permutation in String](../problems/0567-permutation-in-string.md) | Medium | ⏳ | Fixed window anagram check |
| 0438 | [Find All Anagrams in a String](../problems/0438-find-all-anagrams-in-a-string.md) | Medium | ⏳ | Fixed window, return positions |
| 0076 | [Minimum Window Substring](../problems/0076-minimum-window-substring.md) | Hard | ⏳ | Variable window minimum |

## Template for New Problem

When adding a sliding window problem:
1. Initialize left = 0, use right to expand window
2. Track window state (hashmap, counter, sum)
3. When condition met, record result and shrink left
4. Continue until right reaches end

## Related Patterns
- **Two Pointers** (subset): Sliding window is a specific two-pointer technique
- **Hashing** (often combined): For frequency-based windows