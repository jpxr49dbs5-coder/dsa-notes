---
id: "0383"
name: "Ransom Note"
patterns: ["hashing"]
difficulty: easy
status: queued
last_seen: null
---

# 0383 - Ransom Note

**Difficulty:** Easy  
**Status:** ⏳ Queued  
**Last Seen:** Never  

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example:**
```
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Notes

Followup to [0242 - Valid Anagram](../problems/0242-valid-anagram.md). One-directional frequency check using `int[26]`.