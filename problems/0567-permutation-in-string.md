---
id: "0567"
name: "Permutation in String"
patterns: ["sliding-window", "hashing"]
difficulty: medium
status: queued
last_seen: null
---

# 0567 - Permutation in String

**Difficulty:** Medium  
**Status:** ⏳ Queued  
**Last Seen:** Never  

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Notes

Followup to [0242 - Valid Anagram](../problems/0242-valid-anagram.md). Fixed sliding window with frequency array.