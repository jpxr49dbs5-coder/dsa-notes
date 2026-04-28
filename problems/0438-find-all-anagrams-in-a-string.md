---
id: "0438"
name: "Find All Anagrams in a String"
patterns: ["sliding-window", "hashing"]
difficulty: medium
status: queued
last_seen: null
---

# 0438 - Find All Anagrams in a String

**Difficulty:** Medium  
**Status:** ⏳ Queued  
**Last Seen:** Never  

## Problem Statement

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Input: s = "abab", p = "ab"
Output: [0,1,2]
```

## Notes

Followup to [0567 - Permutation in String](../problems/0567-permutation-in-string.md). Return all positions instead of boolean.