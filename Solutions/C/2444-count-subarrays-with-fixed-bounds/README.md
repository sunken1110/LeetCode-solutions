**Count Subarrays With Fixed Bounds**
=
[Problem Link](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description)

## Intuition
Consider a single scanning of `nums`. Suppose we find the 1st `minK` at index `i` and then find 1st `maxK`
at index `j`. Then `[nums[i], ..., nums[j]` is a minimal size of required fixed-bound subarray. To count the possible 
number of fixed-bound subarray with left-side expansion, we need to find an index `k` such that `nums[k] > maxK` or 
`nums[k] < minK` and the count is `j-k+1`. To sum up, with fixed `left` index, start scanning the current index `i` 
and `j` as `curr_min` and `curr_max`. If we meet a candidate of `k` then, reset both `curr_min` and `curr_max` and 
adjust `left` to `k+1`. Again search both `curr_min` and `curr_max` until new `k` is found.

## Approach
**Step-by-Step Process**

1. Initialize `curr_min`, `curr_min`, `left`.

2. In a single scanning of `nums`, check if the `num` is `minK` or `maxK` or outsider of the range.
    - If `minK`, then update `curr_min`.
    - If `maxK`, then update `curr_max`.
    - If `num` lies on the ouside of the range, then reset `curr_min`, `curr_max`. `left` should be the next index.

3. For each step, count the number of fixed-bound subarray as `min(curr_min, curr_max) - left + 1`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        curr_min = -1
        curr_max = -1
        left = 0
        cnt = 0

        for right, num in enumerate(nums):
            if num == minK:
                curr_min = right

            if num == maxK:
                curr_max = right

            if num < minK or num > maxK:
                left = right + 1
                curr_min = -1
                curr_max = -1

            if curr_min != -1 and curr_max != -1:
                cnt += min(curr_min, curr_max) - left + 1

        return cnt
```
