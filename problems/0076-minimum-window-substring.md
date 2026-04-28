---
id: "0076"
name: "Minimum Window Substring"
patterns: ["sliding-window"]
difficulty: hard
status: queued
last_seen: null
---

# 0076 - Minimum Window Substring

**Difficulty:** Hard  
**Status:** ⏳ Queued  
**Last Seen:** Never  

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

**Example:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
```

## Notes

Hardest in the anagram family. Variable-size sliding window containing all characters of `t`.