---
id: "0242"
name: "Valid Anagram"
patterns: ["hashing"]
difficulty: easy
status: solved
last_seen: 2026-04-27
---

# 0242 - Valid Anagram

**Difficulty:** Easy | **Status:** ✅ Solved | **Last Seen:** 2026-04-27
**Pattern:** [Frequency Counting](../patterns/frequency-counting.md)

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`.
Constraints: lowercase English letters only.

## Approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| Sort + compare | O(n log n) | O(n) | Simple but suboptimal |
| HashMap frequency | O(n) | O(n) | Correct, handles Unicode |
| `int[26]` array ✅ | O(n) | O(1) | Optimal — fixed charset |

**Why O(1) space:** `int[26]` is always 26 integers regardless of input length.
`ch - 'a'` maps each character to a fixed index — same intuition as index-as-hash (LC 442).

## My Solution (Java)

**Runtime:** 2ms — beats 99.62% | **Memory:** 44.79MB

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] letterCnt = new int[26];
        for (char c : s.toCharArray()) letterCnt[c - 'a']++;
        for (char c : t.toCharArray()) letterCnt[c - 'a']--;
        for (int n : letterCnt) if (n != 0) return false;
        return true;
    }
}
```

## Traps

- Skip length check → wastes two full iterations before failing.
- `letterCnt[i] > 0` in final check → misses when `t` has chars `s` doesn't (count goes negative).
- Using HashMap when constraint says lowercase only → correct but O(n) space, misses the trick.

## Unicode Follow-up

`int[26]` breaks for Unicode. Switch to HashMap — space becomes O(k) unique chars.

```java
Map<Character, Integer> map = new HashMap<>();
for (char c : s.toCharArray()) map.merge(c, 1, Integer::sum);
for (char c : t.toCharArray()) map.merge(c, -1, Integer::sum);
for (int count : map.values()) if (count != 0) return false;
return true;
```

## Follow-ups (Queued)

- [ ] [0383 - Ransom Note](../problems/0383-ransom-note.md)
  Same `int[26]` trick, one-directional check. Easy warm-up.
  **Time:** O(n) **Space:** O(1)

- [ ] [0567 - Permutation in String](../problems/0567-permutation-in-string.md)
  Does any permutation of `s1` exist in `s2`? Fixed sliding window + frequency array. Do before 438.
  **Pattern:** Sliding Window + Frequency Counting | **Time:** O(n) **Space:** O(1)

- [ ] [0438 - Find All Anagrams in a String](../problems/0438-find-all-anagrams.md)
  Same as 567 but return all positions instead of bool.
  **Time:** O(n) **Space:** O(1)

- [ ] [0049 - Group Anagrams](../problems/0049-group-anagrams.md)
  Scale to a list of strings — use sorted string or frequency tuple as HashMap key.
  **Pattern:** Hashing | **Time:** O(n · k log k) **Space:** O(n · k)

- [ ] [0076 - Minimum Window Substring](../problems/0076-minimum-window-substring.md)
  Variable-size window containing all chars of `t`. Hardest of this family. Attempt after 567 and 438.
  **Time:** O(n) **Space:** O(k)

## Pattern Evolution Chain

```
242 (two strings anagram?)
      ↓ find inside larger string
567 (permutation exists in s2? → bool)
      ↓ return all positions
438 (all anagram start indices)
      ↓ variable window
076 (minimum window substring) ← hardest
      ↓ scale to many strings
049 (group anagrams)
```

## Interviewer Escalation

- "What if Unicode?" → HashMap, O(k) space
- "What if input is a stream?" → can't sort, frequency map only
- "Find all anagrams in a larger string?" → LC 438, sliding window