---
id: "0217"
name: "Contains Duplicate"
patterns: ["hashing"]
difficulty: easy
status: solved
last_seen: 2026-04-27
---

# 0217 - Contains Duplicate

**Difficulty:** Easy  
**Status:** ✅ Solved  
**Last Seen:** 2026-04-27  

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example:**
```
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
```

## Clarifying qs
1. What if the array is empty or has one element? — expected: handle gracefully, return False
2. Can values be negative? — matters for the index-as-hash trick in harder variants
3. What if we can't use extra space? — pivots you toward sorting or in-place approaches
4. Does order matter? — no, but good to confirm; sets don't preserve order and that's fine here


## Solution Approach

**Pattern:** [Hashing](../patterns/hashing.md)

Use a hash set to track seen elements:
1. Iterate through the array
2. For each number, check if it's already in the set
3. If yes, return `true` (duplicate found)
4. Otherwise, add it to the set
5. If loop completes, return `false` (no duplicates)

**Time:** O(n)  
**Space:** O(n)

## Code Example

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // what is the range of nums length
        // is the nums array sorted?
        
        // brute force t: O(N^2) s : O(1)
        for (int i =0; i<nums.length; i++) {
            for (int j =i+1; j<nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;

        // using set / space t= O(N) s: O(N)
        Set<Integer> numExists = new HashSet<>();
        for (int i =0;i<nums.length;i++) {
            if (numExists.contains(nums[i])) {
                return true;
            }
            numExists.add(nums[i]);
        }
        return false;

        // sorting 
        // t: O(nlogn) s: O(1)
        Arrays.sort(nums);
        for (int i =0; i<nums.length-1; i++) {
            if (nums[i] == nums[i+1] ) {
                return true;
            }
        }
        return false;
    }
}
```

## Follow-ups (Queued)

- [ ] [0442 - Find All Duplicates in an Array](../problems/0442-find-all-duplicates-in-array.md) — return all duplicates (in-place trick)

## Follow-ups (Queued)

- [ ] [0219 - Contains Duplicate II](../problems/0219-contains-duplicate-ii.md) — index-constrained variant
- [ ] [0220 - Contains Duplicate III](../problems/0220-contains-duplicate-iii.md) — value + index constraints

## Notes

This is the foundational problem in the Contains Duplicate progression chain. Once you understand this, 219 and 220 add constraints.

**Key insight:** Hash set gives O(1) lookup — you could also sort and compare adjacent elements for O(n log n) time but O(1) space trade-off.
