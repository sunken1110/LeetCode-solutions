**Maximum Erasure Value**
=
[Problem Link](https://leetcode.com/problems/maximum-erasure-value/description)

## Intuition
Since a valid subarray contains unique characters, we can use a sliding window technique. Extend the right window 
until any duplication found. If found, then shrink the left window until the duplicated character disappears. 
For each window get a score and take the maximum of it.

## Approach
**Step-by-Step Process**

1. Initialize already seen characters `unique` and score `score`.

2. Start from the window `l=0`, extend until no duplication found. Add `num` to `unique`.
    - Add `num` to `score`, and take the maximum `score`.

3. If a new `num` is already in `unique`, then delete the left-side integers of previous `num` and itself from `unique`.
    - Subtract deleted integers from `score`.
  
4. Repeat until every integer is checked, and return the maximum `score`. 
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        max_score = 0
        unique = set()
        l = 0

        for num in nums:
            while num in unique:
                unique.remove(nums[l])
                score -= nums[l]
                l += 1

            unique.add(num)
            score += num
            max_score = max(max_score, score)

        return max_score
```
