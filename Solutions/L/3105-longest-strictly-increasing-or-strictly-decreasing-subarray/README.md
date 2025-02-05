**Longest Strictly Increasing or Strictly Decreasing Subarray**
=
[Problem Link](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description)

## Intuition
We scan the array 2 times; checking strictly increasing subarrays, and checking strictly decreasing subarrays. 
In each scanning, we cumulatively count the length of strictly inc./dec. subarray and take a maximum value.

## Approach
**Step-by-Step Process**

1. Set `max_len` of maximum length of strictly increasing subarray and current length of strictly increasing subarray.

2. Scan whole given array `nums`, and record a maximum length.

3. Repeat now for the maximum length of strictly decreasing subarray, and record a maximum length (including *2.*).
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 1

        # strictly increasing case
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 1

        #strictrly decreasing case
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)

            else:
                curr_len = 1

        return max_len
```
