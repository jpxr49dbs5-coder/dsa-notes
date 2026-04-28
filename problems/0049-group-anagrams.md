---
id: "0049"
name: "Group Anagrams"
patterns: ["hashing"]
difficulty: medium
status: queued
last_seen: null
---

# 0049 - Group Anagrams

**Difficulty:** Medium  
**Status:** ⏳ Queued  
**Last Seen:** Never  

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

## Notes

Followup to [0242 - Valid Anagram](../problems/0242-valid-anagram.md). Use sorted string as hash key to group anagrams.