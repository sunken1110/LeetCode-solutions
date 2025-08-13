**Smallest Subarrays With Maximum Bitwise OR**
=
[Problem Link](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description)

## Intuition
Suppose we have an index `i` and want to check for each `j < i`, `i` is the minimum index of maximum bitwise OR. 
Note that `i` is the maximum bitwise OR if `nums[i] | nums[j]` = `nums[i]` for every `j`. Then for each step `i`, we 
find a smaller index `j` such that `i` is the target minimized index. Also update each `nums[j]` to avoid abundant 
tracking by bitwise OR `nums[i]`.

## Approach
**Step-by-Step Process**

1. Initialize `ans = [1] * n` since the length of subarray is at least 1.

2. For each index `i`, check every smaller index `j` until the maximum bitwise OR value is differ.
    - Update `nums[j]` by maximum bitwise OR `nums[i]`.
    - Each minimized size is `i-j+1`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            j = i-1

            while j >= 0 and nums[j] | nums[i] != nums[j]:
                ans[j] = i-j+1
                nums[j] |= nums[i]
                j -= 1

        return ans
```
