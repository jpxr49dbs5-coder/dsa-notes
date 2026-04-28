---
id: "0442"
name: "Find All Duplicates in an Array"
patterns: ["hashing"]
difficulty: medium
status: solved
last_seen: 2026-04-27
---

# 0442 - Find All Duplicates in an Array

**Difficulty:** Medium
**Status:** ✅ Solved
**Last Seen:** 2026-04-27

## Problem Statement

Given an integer array `nums` of length `n` where all integers are in the range `[1, n]`
and each integer appears once or twice, return an array of all integers that appear twice.

Must run in O(n) time and use only O(1) extra space (output list excluded).

## My Solution (Java)

**Approach taken:** Hash map storing value → index, then tombstoning visited cells with -1.

```java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        // brute force
        Set<Integer> result = new HashSet<>();
        for (int i =0;i<nums.length; i++) {
            for (int j =i+1;j<nums.length;j++) {
                if (nums[i] == nums[j]) {
                    result.add(nums[i]);
                }
            }
        }
        return new ArrayList(result);

        // using set
        Set<Integer> seen = new HashSet<>();
        Set<Integer> skip = new HashSet<>();
        List<Integer> result = new ArrayList<>();
        for (int num: nums) {
            if (seen.contains(num) && !skip.contains(num)) {
                result.add(num);
                skip.add(num);
                seen.remove(num);
            }
            seen.add(num);
        }
        return result;

        Map<Integer, Integer> seen = new HashMap<>();
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (seen.get(nums[i]) != null && nums[seen.get(nums[i])] != -1) {
                result.add(nums[i]);
                nums[seen.get(nums[i])] = -1;
            }
            seen.put(nums[i], i);
        }
        return result;
    }
}
```

**Time:** O(n)
**Space:** O(n) ← the HashMap. Does NOT meet the O(1) space constraint.

### Honest assessment of my approaches

| Attempt | Strategy | Time | Space | Verdict |
|---|---|---|---|---|
| Brute force (commented) | Nested loops + set | O(n²) | O(n) | Too slow |
| Set-based (commented) | seen + skip sets | O(n) | O(n) | Correct, cleaner |
| Final (submitted) | HashMap + tombstone | O(n) | O(n) | Correct but over-engineered |
| Optimal (not reached) | Sign marking in-place | O(n) | O(1) | What to aim for |

The tombstone idea (`nums[seen.get(nums[i])] = -1`) shows you were thinking
about in-place marking — you just applied it through the HashMap instead of
directly via the `[1, n]` constraint. That's the key insight one step away.

## Optimal Solution

**Pattern:** [Hashing](../patterns/hashing.md)

Values are in `[1, n]`, so every value maps to a valid index: `abs(num) - 1`.
Use the sign of that cell as a visited flag — negate on first visit,
already negative on second visit means duplicate.

```java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();
        for (int num : nums) {
            int idx = Math.abs(num) - 1;
            if (nums[idx] < 0) {
                result.add(Math.abs(num));
            } else {
                nums[idx] *= -1;
            }
        }
        return result;
    }
}
```

**Time:** O(n)
**Space:** O(1) ✅

## Follow-ups (Queued)

- [ ] [0448 - Find All Numbers Disappeared in an Array](../problems/0448-find-all-numbers-disappeared.md) — inverse problem using the same sign-marking trick
- [ ] [0041 - First Missing Positive](../problems/0041-first-missing-positive.md) — escalation to placement-based index hashing

### Why this works

```
nums = [4, 3, 2, 7, 8, 2, 3, 1]
         0  1  2  3  4  5  6  7   ← indices

See 4 → negate nums[3]:  [4,  3,  2, -7,  8,  2,  3,  1]
See 3 → negate nums[2]:  [4,  3, -2, -7,  8,  2,  3,  1]
See 2 → negate nums[1]:  [4, -3, -2, -7,  8,  2,  3,  1]
See 7 → negate nums[6]:  [4, -3, -2, -7,  8,  2, -3,  1]
See 8 → negate nums[7]:  [4, -3, -2, -7,  8,  2, -3, -1]
See 2 → nums[1] = -3 < 0 → DUPLICATE → append 2
See 3 → nums[2] = -2 < 0 → DUPLICATE → append 3
See 1 → negate nums[0]:  [-4, -3, -2, -7,  8,  2, -3, -1]

Result: [2, 3] ✅
```

## Traps

- Using `num` instead of `Math.abs(num)` for the index — values get negated
  mid-traversal, so raw `num` will be negative on revisit. Always take abs first.
- Using `num` instead of `Math.abs(num)` when appending — same reason.
- Applying this trick when values are NOT in `[1, n]` — won't work. Always
  verify the constraint before using index-as-hash.
- Interviewer may ask you to restore the array — second pass, negate everything
  back to positive.

## The Gap: My Solution vs Optimal

My final attempt was one insight away. I used `nums[seen.get(nums[i])] = -1`
to tombstone visited positions — exactly the right instinct — but routed through
a HashMap instead of using the value itself as the index. The `[1, n]` constraint
makes the HashMap completely unnecessary: the value IS the index.

**The leap:** drop the HashMap, compute `idx = Math.abs(num) - 1` directly.

## Notes

The sign-marking trick is a member of a broader family: "use the array as
its own hash map when values are bounded by length." Any time you see
`values in [1, n]` with an O(1) space requirement, this should be your
first thought.

My brute force and set approaches were both reasonable first steps.
The set-based approach (commented) is actually cleaner than my final HashMap
version — simpler logic, same complexity. The HashMap added complexity
without benefit. When stuck between approaches, prefer the simpler one
that meets constraints.

**Interviewer escalation path:** "Can you do it without extra space?" → sign marking.
"Can you restore the array?" → second pass. "What if values aren't in [1, n]?" →
forced back to O(n) space, no trick possible.